# Generated by Django 5.1.2 on 2024-11-25 18:46

import timezone_field.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0092_targetvertex_player_id_targetvertex_village_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="server",
            name="tz",
            field=timezone_field.fields.TimeZoneField(
                default="Europe/Warsaw", use_pytz=False
            ),
        ),
    ]
