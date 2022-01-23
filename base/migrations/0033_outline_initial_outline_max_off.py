# Generated by Django 3.2.11 on 2022-01-23 17:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0032_remove_profile_server_bind_remind_not_before_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='outline',
            name='initial_outline_max_off',
            field=models.IntegerField(default=28000, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(28000)]),
        ),
    ]
