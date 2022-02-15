# Generated by Django 4.0.2 on 2022-02-15 15:04

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0033_outline_initial_outline_max_off"),
    ]

    operations = [
        migrations.AddField(
            model_name="outline",
            name="morale_on_targets_greater_than",
            field=models.IntegerField(
                default=100,
                validators=[
                    django.core.validators.MinValueValidator(25),
                    django.core.validators.MaxValueValidator(100),
                ],
            ),
        ),
        migrations.AddField(
            model_name="player",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="player",
            name="points",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="player",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="player",
            name="villages",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="tribe",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="tribe",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="villagemodel",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="villagemodel",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="world",
            name="etag_player",
            field=models.CharField(default="", max_length=200),
        ),
        migrations.AddField(
            model_name="world",
            name="etag_tribe",
            field=models.CharField(default="", max_length=200),
        ),
        migrations.AddField(
            model_name="world",
            name="etag_village",
            field=models.CharField(default="", max_length=200),
        ),
    ]
