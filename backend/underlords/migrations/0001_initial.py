# Generated by Django 2.2.5 on 2019-09-13 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alliances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=80, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Heroes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier', models.IntegerField()),
                ('name', models.TextField(max_length=80, unique=True)),
                ('brazilian_name', models.TextField(max_length=80, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HeroesAlliances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alliance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='underlords.Alliances')),
                ('hero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='underlords.Heroes')),
            ],
            options={
                'unique_together': {('hero', 'alliance')},
            },
        ),
        migrations.CreateModel(
            name='AlliancesEffects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('effect', models.TextField()),
                ('alliance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='underlords.Alliances')),
            ],
            options={
                'unique_together': {('alliance', 'quantity')},
            },
        ),
    ]
