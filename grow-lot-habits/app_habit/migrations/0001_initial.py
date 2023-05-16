# Generated by Django 4.2 on 2023-05-03 13:23

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
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=128, verbose_name='description')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='habit created')),
                ('place', models.CharField(default='', max_length=128, verbose_name='place')),
                ('time', models.TimeField(default='12:00', max_length=100, verbose_name='time')),
                ('action', models.CharField(default='', max_length=128, verbose_name='action')),
                ('pleasure_habit', models.BooleanField(default=False, verbose_name='pleasure habit')),
                ('binded_habit', models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='binded habit')),
                ('periodic_habit', models.PositiveSmallIntegerField(default=7, verbose_name='periodic habit')),
                ('reward', models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='reward')),
                ('time_for_finishing', models.PositiveSmallIntegerField(default=1, verbose_name='time for finishing')),
                ('is_public', models.BooleanField(default=False, verbose_name='public or not')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='habit_create', to=settings.AUTH_USER_MODEL, verbose_name='author')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='habit_update', to=settings.AUTH_USER_MODEL, verbose_name='last updated by')),
            ],
            options={
                'verbose_name': 'habit',
                'verbose_name_plural': 'habitы',
            },
        ),
    ]
