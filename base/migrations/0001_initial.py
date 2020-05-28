# Generated by Django 3.0.6 on 2020-05-27 22:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.IntegerField()),
                ('name', models.TextField()),
                ('tribe_id', models.IntegerField()),
                ('villages', models.IntegerField()),
                ('points', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('world', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tribe_id', models.IntegerField()),
                ('name', models.TextField()),
                ('tag', models.TextField()),
                ('members', models.IntegerField()),
                ('villages', models.IntegerField()),
                ('points', models.IntegerField()),
                ('all_points', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('world', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('village_id', models.IntegerField()),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('player_id', models.IntegerField()),
                ('world', models.IntegerField()),
                ('points', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='World',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Tytuł')),
                ('world', models.IntegerField(verbose_name='Numer świata')),
            ],
            options={
                'ordering': ('-world',),
            },
        ),
        migrations.CreateModel(
            name='New_Outline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_akcji', models.DateField()),
                ('nazwa', models.TextField()),
                ('swiat', models.CharField(choices=[], max_length=6)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=8)),
                ('moje_plemie_skrot', models.CharField(default='', max_length=100, null=True)),
                ('przeciwne_plemie_skrot', models.CharField(default='', max_length=100, null=True)),
                ('zbiorka_wojsko', models.TextField(default='', help_text="Wymagana dokładna forma ze skryptu Wojska, zajrzyj do <a href='/dokumentacja'>dokumentacji</a>", null=True)),
                ('zbiorka_obrona', models.TextField(default='', help_text="Wymagana dokładna forma ze skryptu Obrona, zajrzyj do <a href='/dokumentacja'>dokumentacji</a>", null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]
