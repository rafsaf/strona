from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path("", views.base_view, name="base"),
    path("profile/user-settings", views.profile_settings, name="settings"),
    path("profile/add-world", views.add_world, name="add_world"),
    path("overview/<str:token>", views.overview, name="overview"),
    path("overview-fail", views.overview_fail, name="overview_fail"),
    path("planer/", views.OutlineList.as_view(), name="planer"),
    path("planer/show-all", views.OutlineListShowAll.as_view(), name="planer_all"),
    path("planer/update", views.database_update, name="planer_update"),
    path("planer/create/", views.new_outline_create, name="planer_create"),
    path("planer/<int:_id>/status", views.inactive_outline, name="planer_status"),
    path("planer/<int:_id>/results", views.outline_detail_results, name="planer_detail_results"),
    path("planer/<int:id1>/<str:token>/change", views.overview_hide_unhide, name="planer_overview_hide"),
    path("planer/<int:_id>", views.outline_detail_1, name="planer_detail"),
    path("planer/<int:_id>/planer-form", views.initial_form, name="planer_initial_form",),
    path("planer/<int:_id>/planer-menu", views.initial_planer, name="planer_initial",),
    path("planer/<int:id1>/create_output", views.create_final_outline, name="planer_output",),
    path("planer/<int:id1>/complete", views.complete_outline, name="planer_complete",),
    path("planer/<int:id1>/update_troops", views.update_outline_troops, name="planer_update_troops",),
    path("planer/planer-menu/<int:pk>", views.InitialDeleteTime.as_view(), name="planer_delete_time",),
    path("planer/<int:id1>/delete_target/<int:id2>", views.delete_target, name="planer_delete_target",),
    path("planer/<int:id1>/change-weight/<int:id2>/", views.change_weight_off, name="planer_change_weight",),
    path("planer/<int:id1>/planer-target/<int:id2>", views.initial_target, name="planer_initial_detail",),
    path("planer/<int:id1>/<int:id2>/<int:id3>/add_first", views.initial_add_first, name="planer_add_first",),
    path("planer/<int:id1>/<int:id2>/<int:id3>/add_first_fake", views.initial_add_first_fake, name="planer_add_first_fake",),
    path("planer/<int:id1>/<int:id2>/<int:id3>/add_last_fake", views.initial_add_last_fake, name="planer_add_last_fake",),
    path("planer/<int:id1>/<int:id2>/<int:id3>/add_last", views.initial_add_last, name="planer_add_last",),
    path("planer/<int:id1>/<int:id2>/<int:id4>/up", views.initial_move_up, name="planer_move_up",),
    path("planer/<int:id1>/<int:id2>/<int:id4>/<int:n>", views.initial_divide, name="planer_divide",),
    path("planer/<int:id1>/<int:id2>/<int:id4>/down", views.initial_move_down, name="planer_move_down",),
    path("planer/<int:id1>/<int:id2>/<int:id4>/delete", views.initial_weight_delete, name="planer_initial_delete",),



    path("planer/<int:_id>/get-deff", views.outline_detail_2_deff, name="planer_detail_get_deff"),
    path("planer/<int:_id>/get-off", views.outline_detail_2_off, name="planer_detail_get_off"),


    path("planer/<int:_id>/create/select-tribe", views.new_outline_create_select, name="planer_create_select",),
    path("planer/<int:_id>/delete/ally-tags",views.outline_delete_ally_tags,name="planer_delete_ally_tags"),
    path("planer/<int:_id>/delete/enemy-tags",views.outline_delete_enemy_tags,name="planer_delete_enemy_tags"),
    path("planer/<int:_id>/disable_editable",views.outline_disable_editable,name="planer_disable_editable"),
    path("planer/<int:pk>/delete", views.OutlineDelete.as_view(), name="planer_delete"),
    path("documentation", views.base_documentation, name="documentation"),
]
