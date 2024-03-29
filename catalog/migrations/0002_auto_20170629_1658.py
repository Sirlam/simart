# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-29 15:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pump',
            fields=[
                ('pump_id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for Pumps', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('crude_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.CrudeType')),
            ],
        ),
        migrations.CreateModel(
            name='StationPump',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pump', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Pump')),
            ],
        ),
        migrations.CreateModel(
            name='StationTank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Station')),
            ],
        ),
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('tank_id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for Tanks', primary_key=True, serialize=False)),
                ('tank', models.CharField(max_length=200)),
                ('crude_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.CrudeType')),
            ],
        ),
        migrations.CreateModel(
            name='TankQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening', models.PositiveIntegerField()),
                ('closing', models.PositiveIntegerField()),
                ('under', models.PositiveIntegerField()),
                ('pump', models.DecimalField(decimal_places=2, max_digits=6)),
                ('new', models.PositiveIntegerField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('tank', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.StationTank')),
            ],
        ),
        migrations.AddField(
            model_name='stationtank',
            name='tank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Tank'),
        ),
        migrations.AddField(
            model_name='stationpump',
            name='tank',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.StationTank'),
        ),
        migrations.AlterUniqueTogether(
            name='stationtank',
            unique_together=set([('station', 'tank')]),
        ),
        migrations.AlterUniqueTogether(
            name='stationpump',
            unique_together=set([('tank', 'pump')]),
        ),
        migrations.AlterUniqueTogether(
            name='pump',
            unique_together=set([('crude_type', 'name')]),
        ),
    ]
