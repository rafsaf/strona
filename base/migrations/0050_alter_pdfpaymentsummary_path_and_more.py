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

# Generated by Django 4.0.4 on 2022-04-25 22:01

from django.db import migrations, models


def delete_all_pdfs(apps, schema_editor):
    PDFPaymentSummary = apps.get_model("base", "PDFPaymentSummary")
    for pdf in PDFPaymentSummary.objects.all():
        pdf.delete()


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0049_pdfpaymentsummary_created_at_and_more"),
    ]

    operations = [
        migrations.RunPython(delete_all_pdfs),
        migrations.AlterField(
            model_name="pdfpaymentsummary",
            name="period",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="pdfpaymentsummary",
            name="path",
            field=models.CharField(max_length=300, primary_key=True, serialize=False),
        ),
    ]
