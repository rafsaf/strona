# Copyright 2021 Rafał Safin (rafsaf). All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

# Generated by Django 3.2.2 on 2021-05-23 23:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0016_weightmaximum_too_far_away"),
    ]

    operations = [
        migrations.AlterField(
            model_name="outline",
            name="initial_outline_front_dist",
            field=models.IntegerField(
                default=10,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(500),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="outline",
            name="initial_outline_maximum_front_dist",
            field=models.IntegerField(
                default=120,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(1000),
                ],
            ),
        ),
    ]
