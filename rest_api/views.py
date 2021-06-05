import datetime
from django.conf import settings
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.utils import timezone
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
import stripe
from base.models import (
    Outline,
    OutlineTime,
    Overview,
    Payment,
    Profile,
    TargetVertex,
    WeightMaximum,
    WeightModel,
)
from rest_api import serializers


class TargetTimeUpdate(APIView):
    """
    For given target id match it with Time obj id.
    """

    permission_classes = [IsAuthenticated]

    def put(
        self, request: HttpRequest, target_id: int, time_id: int, format=None
    ) -> Response:
        target: TargetVertex = get_object_or_404(TargetVertex, pk=target_id)
        outline_time: OutlineTime = get_object_or_404(
            OutlineTime.objects.select_related("outline"),
            pk=time_id,
            outline__owner=request.user,
        )
        old_id: str

        if target.outline_time is None:
            old_id = "none"
        else:
            old_id = f"{target.pk}-time-{target.outline_time.pk}"

        target.outline_time = outline_time
        target.save()

        return Response(
            {"new": f"{target.pk}-time-{time_id}", "old": old_id},
            status=status.HTTP_200_OK,
        )


class TargetDelete(APIView):
    """
    For given target id, delete obj.
    """

    permission_classes = [IsAuthenticated]

    def delete(self, request: HttpRequest, target_id: int, format=None) -> Response:
        target: TargetVertex = get_object_or_404(
            TargetVertex.objects.select_related("outline"), pk=target_id
        )
        outline: Outline = get_object_or_404(
            Outline, owner=request.user, pk=target.outline.pk
        )

        weights = WeightModel.objects.filter(target=target)
        # deletes weights related to this target and updates weight state
        weight_model: WeightModel
        for weight_model in weights:
            state: WeightMaximum = weight_model.state
            state.off_left += weight_model.off
            state.off_state -= weight_model.off
            state.nobleman_left += weight_model.nobleman
            state.nobleman_state -= weight_model.nobleman
            state.catapult_left += weight_model.catapult
            state.catapult_state -= weight_model.catapult
            state.save()

        weights.delete()
        target.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OverwiewStateHideUpdate(APIView):
    """
    For given target id, delete obj.
    """

    permission_classes = [IsAuthenticated]

    def put(
        self, request: HttpRequest, outline_id: int, token: str, format=None
    ) -> Response:
        outline: Outline = get_object_or_404(Outline, id=outline_id, owner=request.user)
        overview: Overview = get_object_or_404(Overview, token=token)

        new_state: bool = not bool(overview.show_hidden)
        name: str
        new_class: str
        if new_state:
            name = "True"
            new_class = "btn btn-light btn-light-no-border md-blue"
        else:
            name = "False"
            new_class = "btn btn-light btn-light-no-border md-error"

        overview.show_hidden = new_state
        overview.save()
        return Response({"name": name, "class": new_class}, status=status.HTTP_200_OK)


class ChangeBuildingsArray(APIView):
    """
    For given outline updates array with buildings.
    """

    permission_classes = [IsAuthenticated]

    def put(self, request, outline_id: int, format=None) -> Response:
        outline: Outline = get_object_or_404(Outline, id=outline_id, owner=request.user)

        buildings_serializer = serializers.ChangeBuildingsArraySerializer(
            data=request.data
        )
        if buildings_serializer.is_valid():
            outline.initial_outline_buildings = buildings_serializer.validated_data[
                "buildings"
            ]
            outline.save()
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)


class ResetUserMessages(APIView):
    """
    For given outline updates array with buildings.
    """

    permission_classes = [IsAuthenticated]

    def put(self, request: HttpRequest, format=None) -> Response:
        profile: Profile = get_object_or_404(Profile, user=request.user)
        profile.messages = 0
        profile.save()
        return Response(status=status.HTTP_200_OK)


class StripeConfig(APIView):
    """Stripe config endpoint"""

    permission_classes = [IsAuthenticated]

    def get(self, request: HttpRequest, format=None) -> Response:
        stripe_config = {"publicKey": settings.STRIPE_PUBLISHABLE_KEY}
        return Response(stripe_config, status=status.HTTP_200_OK)


class StripeCheckoutSession(APIView):
    """Stripe checkout session endpoint"""

    permission_classes = [IsAuthenticated]

    def get(self, request: HttpRequest, amount: int, format=None) -> Response:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        if not amount in [30, 55, 70]:
            return Response(status=400)
        price_id: str = settings.STRIPE_PAYMENTS[amount]
        host = request.get_host()
        user_pk: int = request.user.pk
        http = "http://"
        success = reverse("base:payment_done")
        cancel = reverse("base:payment_cancelled")
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=f"{http}{host}{success}",
                cancel_url=f"{http}{host}{cancel}",
                client_reference_id=user_pk,
                payment_method_types=["card", "p24"],
                mode="payment",
                line_items=[
                    {
                        "quantity": 1,
                        "price": price_id,
                    }
                ],
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            session_id = checkout_session["id"]  # type: ignore
            return Response({"sessionId": session_id}, status=status.HTTP_200_OK)


class StripeWebhook(APIView):
    """Stripe checkout session endpoint"""

    permission_classes = [AllowAny]

    def post(self, request: HttpRequest, format=None) -> Response:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
        payload = request.body
        sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")
        if sig_header is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        event = None

        try:
            event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
        except ValueError as e:
            # Invalid payload
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except stripe.error.SignatureVerificationError as e:  # type: ignore
            # Invalid signature
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # Handle the checkout.session.completed event
        if event["type"] == "checkout.session.completed":
            evt_id: str = event["id"]
            if not Payment.objects.filter(event_id=evt_id).exists():
                data: dict = event["data"]["object"]
                user: User = User.objects.get(pk=data["client_reference_id"])
                current_date: datetime.date = timezone.localdate()
                months: int = 0
                amount: int = int(data["amount_total"]) // 100

                if amount == 70:
                    months = 3
                elif amount == 55:
                    months = 2
                elif amount == 30:
                    months = 1
                else:
                    raise ValueError("Not known amount of money")
                Payment.objects.create(
                    user=user,
                    amount=amount,
                    months=months,
                    payment_date=current_date,
                    event_id=evt_id,
                )

        return Response(status=200)
