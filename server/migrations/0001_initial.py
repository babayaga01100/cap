# Generated by Django 4.2.5 on 2023-10-23 07:51

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
            name='SmartFarmSensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remotepower', models.BooleanField()),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('light', models.IntegerField()),
                ('soil', models.IntegerField()),
                ('ledpower', models.BooleanField()),
                ('ledstate', models.BooleanField()),
                ('ledtoggle', models.BooleanField()),
                ('ledautotoggle', models.BooleanField()),
                ('ledstarttimevalue', models.IntegerField()),
                ('ledstartminutevalue', models.IntegerField()),
                ('ledendtimevalue', models.IntegerField()),
                ('ledendminutevalue', models.IntegerField()),
                ('waterpumppower', models.BooleanField()),
                ('waterpumpstate', models.BooleanField()),
                ('waterpumptoggle', models.BooleanField()),
                ('waterpumpautotoggle', models.BooleanField()),
                ('waterpumpstarttime', models.IntegerField()),
                ('waterpumprunningtime', models.IntegerField()),
                ('waterlevelvoltage', models.FloatField()),
                ('watertemperature', models.FloatField()),
                ('fanpower', models.BooleanField()),
                ('fanstate', models.BooleanField()),
                ('fantoggle', models.BooleanField()),
                ('fanautotoggle', models.BooleanField()),
                ('fanstarttimevalue', models.IntegerField()),
                ('fanstartminutevalue', models.IntegerField()),
                ('fanendtimevalue', models.IntegerField()),
                ('fanendminutevalue', models.IntegerField()),
                ('doorpower', models.BooleanField()),
                ('doorstate', models.BooleanField()),
                ('doortoggle', models.BooleanField()),
                ('doorautotoggle', models.BooleanField()),
                ('doorstarttimevalue', models.IntegerField()),
                ('doorstartminutevalue', models.IntegerField()),
                ('doorendtimevalue', models.IntegerField()),
                ('doorendminutevalue', models.IntegerField()),
                ('waterlevelwarning', models.TextField()),
                ('watertempwarning', models.TextField()),
                ('tempwarning', models.TextField()),
                ('humwarning', models.TextField()),
                ('soilwarning', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SmartFarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sfid', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
