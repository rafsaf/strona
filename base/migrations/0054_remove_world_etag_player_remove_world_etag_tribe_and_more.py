# Copyright 2023 Rafał Safin (rafsaf). All Rights Reserved.
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

# Generated by Django 4.0.4 on 2022-05-08 10:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0053_remove_weightmodel_t1_remove_weightmodel_t2"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="world",
            name="etag_player",
        ),
        migrations.RemoveField(
            model_name="world",
            name="etag_tribe",
        ),
        migrations.RemoveField(
            model_name="world",
            name="etag_village",
        ),
        migrations.AddField(
            model_name="world",
            name="fanout_key_text_player",
            field=models.CharField(default="__0", max_length=200),
        ),
        migrations.AddField(
            model_name="world",
            name="fanout_key_text_tribe",
            field=models.CharField(default="__0", max_length=200),
        ),
        migrations.AddField(
            model_name="world",
            name="fanout_key_text_village",
            field=models.CharField(default="__0", max_length=200),
        ),
    ]
