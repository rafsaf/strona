# Generated by Django 4.0.4 on 2022-06-06 08:38

import django.db.models.deletion
from django.db import migrations, models


def create_troops_history_for_all_outlines(apps, schema_editor):
    Outline = apps.get_model("base", "Outline")
    TroopsHistory = apps.get_model("base", "TroopsHistory")
    for outline in Outline.objects.all():
        TroopsHistory.objects.create(outline=outline)


def reverse_migration_pass(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0056_alter_outline_initial_outline_catapult_default"),
    ]

    operations = [
        migrations.CreateModel(
            name="TroopsHistory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("history_json", models.JSONField(default=dict)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "outline",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="base.outline"
                    ),
                ),
            ],
        ),
        migrations.RunPython(
            create_troops_history_for_all_outlines, reverse_migration_pass
        ),
    ]
