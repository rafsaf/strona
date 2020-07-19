""" views.py """


from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.views.decorators.http import require_POST
from django.forms.models import model_to_dict
from django.core.paginator import Paginator

from markdownx.utils import markdownify
from plemiona_pliki.database_update import cron_schedule_data_update
from plemiona_pliki.get_deff import get_deff
import plemiona_pliki.outline_initial as initial
from . import models, forms


class OutlineList(LoginRequiredMixin, ListView):
    """ login required view /planer """

    template_name = "base/base_planer.html"

    def get_queryset(self):
        return (
            User.objects.get(username=self.request.user.username)
            .new_outline_set.all()
            .filter(status="active")
        )


class OutlineListShowAll(LoginRequiredMixin, ListView):
    """ login required view which shows hidden instances /planer/show_all """

    template_name = "base/base_planer.html"

    def get_queryset(self):
        return User.objects.get(
            username=self.request.user.username
        ).new_outline_set.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["show_all"] = True
        return context


@login_required
@require_POST
def inactive_outline(request, _id):
    """ class based view makeing outline with id=id inavtive/active, post and login required """

    outline = get_object_or_404(models.New_Outline, id=_id, owner=request.user)
    if outline.status == "active":
        outline.status = "inactive"
        outline.save()
        return redirect("base:planer")
    else:
        outline.status = "active"
        outline.save()
        return redirect("base:planer_all")


class OutlineDelete(LoginRequiredMixin, DeleteView):
    """ class based view to delete outline login required"""

    def get_queryset(self):
        return User.objects.get(
            username=self.request.user.username
        ).new_outline_set.all()

    def get_success_url(self):
        return reverse("base:planer")


class WorldList(ListView):
    """ class based view to show all worlds """

    model = models.World
    template_name = "base/world/world.html"


def base_view(request):
    """ base view """
    return render(request, "base/base.html")


def base_documentation(request):
    """ base documentation view"""
    doc = models.Documentation.objects.get(title="Doc").main_page
    doc = markdownify(doc)

    context = {"doc": doc}
    return render(request, "base/documentation.html", context)


@login_required
def new_outline_create_select(request, _id):
    """ select user's ally and enemy tribe after creating outline, login required """

    instance = get_object_or_404(models.New_Outline, pk=_id, owner=request.user)

    form1 = forms.Moje_plemie_skrot_Form(request.POST or None)
    form1.fields["plemie1"].choices = [("banned", "--------")] + [
        ("{}".format(i.tag), "{}".format(i.tag))
        for i in models.Tribe.objects.all()
        .filter(world=instance.swiat)
        .exclude(tag__in=instance.moje_plemie_skrot.split(", "))
        .exclude(tag__in=instance.przeciwne_plemie_skrot.split(", "))
    ]

    form2 = forms.Przeciwne_plemie_skrot_Form(request.POST or None)
    form2.fields["plemie2"].choices = [("banned", "--------")] + [
        ("{}".format(i.tag), "{}".format(i.tag))
        for i in models.Tribe.objects.all()
        .filter(world=instance.swiat)
        .exclude(tag__in=instance.przeciwne_plemie_skrot.split(", "))
        .exclude(tag__in=instance.moje_plemie_skrot.split(", "))
    ]

    if "form-1" in request.POST:

        if form1.is_valid():
            plemie = request.POST.get("plemie1")
            if instance.moje_plemie_skrot == "":
                instance.moje_plemie_skrot = plemie
            else:
                instance.moje_plemie_skrot += str(", " + plemie)
            instance.save()
            return redirect("base:planer_create_select", _id)
    if "form-2" in request.POST:
        if form2.is_valid():
            plemie = request.POST.get("plemie2")
            if instance.przeciwne_plemie_skrot == "":
                instance.przeciwne_plemie_skrot = plemie
            else:
                instance.przeciwne_plemie_skrot += str(", " + plemie)
            instance.save()
            return redirect("base:planer_create_select", _id)

    context = {
        "form1": form1,
        "form2": form2,
    }
    return render(request, "base/new_outline/new_outline_create_select.html", context)


@login_required
def new_outline_create(request):
    """ creates new user's outline login required """
    form1 = forms.New_Outline_Form(request.POST or None)
    form1.fields["swiat"].choices = [
        ("{}".format(i.world), "{}".format(i.world)) for i in models.World.objects.all()
    ]

    if form1.is_valid():
        user_ = get_object_or_404(User, username=request.user.username)

        new_instance = models.New_Outline(
            owner=user_,
            data_akcji=request.POST["data_akcji"],
            nazwa=request.POST["nazwa"],
            swiat=request.POST["swiat"],
        )

        new_instance.save()
        results = models.Results(outline=new_instance)
        results.save()
        return render(
            request,
            "base/new_outline/new_outline_create.html",
            {"created": True, "id": new_instance.id},
        )

    context = {"form1": form1}

    return render(request, "base/new_outline/new_outline_create.html", context)


def database_update(request):
    # ZMIENIC
    """ to update database manually, superuser required """
    if request.user.is_superuser:
        cron_schedule_data_update()
        return redirect("base:base")
    else:
        return Http404()


@login_required
def outline_detail_1(request, _id):
    """details user's outline , login required"""

    instance = get_object_or_404(models.New_Outline, id=_id, owner=request.user)

    form1 = forms.Wojsko_Outline_Form(request.POST or None)
    form2 = forms.Obrona_Outline_Form(request.POST or None)

    if "form-1" in request.POST:
        if form1.is_valid():
            instance.zbiorka_wojsko = request.POST.get("zbiorka_wojsko")
            instance.save()

            return redirect("base:planer_detail", _id)

    if "form-2" in request.POST:
        if form2.is_valid():
            instance.zbiorka_obrona = request.POST.get("zbiorka_obrona")
            instance.save()

            return redirect("base:planer_detail", _id)
    context = {"instance": instance, "form1": form1, "form2": form2}

    error = request.session.get("error")
    if not error is None:
        context["error"] = error
        del request.session["error"]
    return render(request, "base/new_outline/new_outline.html", context)


@login_required
def outline_detail_2_deff(request, _id):
    """ details user outline, get deff page """
    instance = get_object_or_404(models.New_Outline, id=_id, owner=request.user)
    results = get_object_or_404(models.Results, pk=instance)

    # only correct zbiorka_obrona allowed
    if instance.zbiorka_obrona == "":
        request.session["error"] = "Zbiórka Obrona pusta !"
        return redirect("base:planer_detail", _id)

    form = forms.Get_Deff_Form(request.POST or None, world=instance.swiat)
    if "form" in request.POST:
        if form.is_valid():
            radius = request.POST.get("radius")
            excluded = request.POST.get("excluded")

            results.results_get_deff = get_deff(instance, int(radius), excluded)
            results.save()

            return redirect("base:planer_detail_get_deff", _id)

    context = {"instance": instance, "form": form}

    return render(request, "base/new_outline/new_outline_get_deff.html", context)


def outline_detail_results(request, _id):
    """ view for results """

    instance = get_object_or_404(models.New_Outline, id=_id, owner=request.user)
    context = {"instance": instance}

    return render(request, "base/new_outline/new_outline_results.html", context)


@login_required
def outline_detail_initial_period_outline(request, _id):
    """ view with form for initial period outline """

    instance = get_object_or_404(models.New_Outline, id=_id, owner=request.user)

    # User have to fill data or get redirected to outline_detail view
    if instance.zbiorka_obrona == "":
        request.session["error"] = "Zbiórka Obrona pusta !"
        return redirect("base:planer_detail", _id)

    if instance.zbiorka_wojsko == "":
        request.session["error"] = "Zbiórka Wojsko pusta !"
        return redirect("base:planer_detail", _id)

    if "form1" in request.POST:
        request.session["pass-to-form"] = "True"
        return redirect("base:planer_initial_form", _id)

    query = [models.Weight.objects.all().filter(target=target) for target in models.Target_Vertex.objects.all().filter(outline=instance)]
    context = {"instance": instance, "query": query}
    return render(request, "base/new_outline/new_outline_initial_period2.html", context)


@login_required
def outline_detail_initial_period_form(request, _id):
    """ view with table with created outline, returned after valid filled form earlier """

    instance = get_object_or_404(models.New_Outline, id=_id, owner=request.user)
    # User have to fill data or get redirected to outline_detail view
    if instance.zbiorka_obrona == "":
        request.session["error"] = "Zbiórka Obrona pusta !"
        return redirect("base:planer_detail", _id)

    if instance.zbiorka_wojsko == "":
        request.session["error"] = "Zbiórka Wojsko pusta !"
        return redirect("base:planer_detail", _id)
    try:
        var = request.session["pass-to-form"]
        allowed_form = True
    except KeyError:
        allowed_form = False

    # always go to the next view after form confirmation OR if user want to
    if allowed_form == False and instance.initial_period_outline_targets != "":
        return redirect("base:planer_initial", _id)

    form1 = forms.Initial_Period_Outline_Player_Form(
        request.POST or None, world=instance.swiat
    )
    form2 = forms.Initial_Period_Outline_Player_Choose_Form(request.POST or None)

    form2.fields["player"].choices = [("banned", "--------")] + [
        ("{}".format(i.name), "{}".format(i.name))
        for i in models.Player.objects.all()
        .exclude(name__in=instance.initial_period_outline_players.split("\r\n"))
        .filter(world=instance.swiat)
        .filter(
            tribe_id__in=[
                tribe.tribe_id
                for tribe in models.Tribe.objects.all().filter(
                    tag__in=instance.moje_plemie_skrot.split(", ")
                )
            ]
        )
    ]

    form1.fields["players"].initial = instance.initial_period_outline_players
    form1.fields["target"].initial = instance.initial_period_outline_targets

    if "form1" in request.POST:
        if form1.is_valid():
            player = request.POST.get("players")
            target = request.POST.get("target")
            max_distance = request.POST.get("max_distance")
            instance.initial_period_outline_players = player
            instance.initial_period_outline_targets = target
            instance.max_distance_initial_outline = max_distance
            instance.save()
            # make outline
            graph = initial.make_outline(instance)
            try:
                del request.session["pass-to-form"]
            except KeyError:
                pass
            return redirect("base:planer_initial", _id)

    if "form2" in request.POST:
        if form2.is_valid():
            player = request.POST.get("player")
            # banned means "-------"
            if player == "banned":
                pass
            elif instance.initial_period_outline_players == "":
                instance.initial_period_outline_players = player
            else:
                instance.initial_period_outline_players += "\r\n{}".format(player)
            instance.save()
            return redirect("base:planer_initial_form", _id)

    context = {"instance": instance, "form1": form1, "form2": form2}
    return render(request, "base/new_outline/new_outline_initial_period1.html", context)


@login_required
def outline_detail_initial_period_outline_detail(request, _id, coord):
    """ view with form for initial period outline detail """
    coordinates = coord[0:3] + "|" + str(coord[3:6])

    instance = get_object_or_404(models.New_Outline, id=_id, owner=request.user)
    target_model = get_object_or_404(
        models.Target_Vertex, outline=instance, target=coordinates
    )

    # User have to fill data or get redirected to outline_detail view
    if instance.zbiorka_obrona == "":
        request.session["error"] = "Zbiórka Obrona pusta !"
        return redirect("base:planer_detail", _id)

    if instance.zbiorka_wojsko == "":
        request.session["error"] = "Zbiórka Wojsko pusta !"
        return redirect("base:planer_detail", _id)

    graph = initial.get_branch_graph(instance, target_model)
    target: initial.Vertex_Represent_Target_Village = graph.get_target_vertex(
        target_model.target
    )

    nonused_vertices = [
        i for i in target.connected_to_vertex_army if i not in target.result_lst
    ]

    # sort
    sort = request.GET.get("sort")
    if sort is None or sort == "distance":
        sort = "distance"
        sorting = "distance"
        rev = False
    elif sort == "distance-r":
        sorting = "distance"
        rev = True
    else:
        sorting = sort
        rev = True

    nonused_vertices.sort(key=lambda weight: getattr(weight, sorting), reverse=rev)
    # paginator
    paginator = Paginator(nonused_vertices, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    result_lst = models.Weight.objects.all().filter(target=target_model)
    # url
    url = (
        reverse("base:planer_initial_detail", args=[_id, coord])
        + f"?page={page_obj.number}&sort={sort}#table"
    )
    # form modal - update / duplicate
    form = forms.Weight_form(request.POST or None)

    if "save" in request.POST:
        if form.is_valid():
            start = request.POST.get("start")
            off = request.POST.get("off")
            snob = request.POST.get("snob")

            obj = models.Weight.objects.get(target=target_model, start=start)
            obj.off = off
            obj.snob = snob
            obj.save()
            return redirect(url)

    if "add-new" in request.POST:
        if form.is_valid():
            start = request.POST.get("start")
            off = request.POST.get("off")
            snob = request.POST.get("snob")
            distance = request.POST.get("distance")
            snob = request.POST.get("snob")

            obj = models.Weight.objects.get(target=target_model, start=start)
            obj.off = off
            obj.snob = snob
            obj.save()
            return redirect(url)

    # raczej zmienic caly ten syf nizej
    for weight in result_lst:
        # usuwanie
        if f"{weight.start}-delete" in request.POST:
            target.delete_element(weight.start)
            target.renew(target_model)

            return redirect(url)

        # up
        if f"{weight.start}-up" in request.POST:
            target.swap_up(weight.start)
            target.renew(target_model)

            return redirect(url)
        # down
        if f"{weight.start}-down" in request.POST:
            target.swap_down(weight.start)
            target.renew(target_model)

            return redirect(url)

    for i in nonused_vertices:
        # add first
        if f"{i.start.kordy}-add-first" in request.POST:
            target.add_first(i.start.kordy)
            target.renew(target_model)

            return redirect(url)
        # add last
        if f"{i.start.kordy}-add-last" in request.POST:
            target.add_last(i.start.kordy)
            target.renew(target_model)

            return redirect(url)

    context = {
        "instance": instance,
        "target": target,
        "nonused": nonused_vertices,
        "result_lst": result_lst,
        "form": form,
        "page_obj": page_obj,
        "sort": sort,
    }
    return render(request, "base/new_outline/new_outline_initial_period3.html", context)
