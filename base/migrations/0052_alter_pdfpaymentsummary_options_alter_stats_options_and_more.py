# Generated by Django 4.0.4 on 2022-04-25 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0051_alter_world_speed_units_alter_world_speed_world"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="pdfpaymentsummary",
            options={
                "verbose_name": "PDF Summary",
                "verbose_name_plural": "PDF Summaries",
            },
        ),
        migrations.AlterModelOptions(
            name="stats",
            options={"verbose_name": "Statistic", "verbose_name_plural": "Statistics"},
        ),
        migrations.AlterModelOptions(
            name="targetvertex",
            options={"verbose_name": "Target", "verbose_name_plural": "Targets"},
        ),
    ]
