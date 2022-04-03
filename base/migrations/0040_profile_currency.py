# Generated by Django 4.0.3 on 2022-04-03 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0039_stripeproduct_stripeprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='currency',
            field=models.CharField(choices=[('PLN', 'PLN'), ('EUR', 'EUR')], default='PLN', max_length=3),
        ),
    ]
