from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt

from base import forms
from base.models import Payment, Profile, Server


@login_required
def add_world(request: HttpRequest) -> HttpResponse:
    user = request.user
    success = request.session.get("world_created")
    form1 = forms.AddNewWorldForm(None)
    if request.method == "POST":
        if "form1" in request.POST:
            form1 = forms.AddNewWorldForm(request.POST)
            if form1.is_valid():
                # already created in form clean()
                request.session["world_created"] = "true"
                return redirect("base:add_world")

    context = {"user": user, "form1": form1, "message": success}
    if success is not None:
        del request.session["world_created"]
    return render(request, "base/user/add_world.html", context=context)


@login_required
def profile_settings(request: HttpRequest) -> HttpResponse:
    user = request.user
    form1 = forms.ChangeServerForm(None)
    if request.method == "POST":
        if "form1" in request.POST:
            form1 = forms.ChangeServerForm(request.POST)
            if form1.is_valid():
                new_server = request.POST.get("server")
                new_server = get_object_or_404(Server, dns=new_server)
                profile: Profile = Profile.objects.get(user=user)
                profile.server = new_server
                profile.save()
                return redirect("base:settings")
    context = {"user": user, "form1": form1}
    return render(request, "base/user/profile_settings.html", context=context)


@login_required
def premium_view(request: HttpRequest) -> HttpResponse:
    user: User = request.user  # type: ignore
    payments = Payment.objects.filter(user=user).order_by("-payment_date", "-new_date")
    context = {"user": user, "payments": payments}
    return render(request, "base/user/premium.html", context=context)


@login_required
@csrf_exempt
def payment_done(request: HttpRequest) -> HttpResponse:
    return render(request, "base/user/payment_done.html")
