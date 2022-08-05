# Generated by Django 4.1 on 2022-08-05 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Port', models.CharField(blank=True, max_length=255, null=True)),
                ('Address', models.TextField(blank=True, null=True)),
                ('DeviceName', models.CharField(blank=True, max_length=255, null=True)),
                ('UserName', models.CharField(default='admin', max_length=255)),
                ('Password', models.CharField(max_length=255)),
                ('deviceType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.devicetype')),
            ],
        ),
    ]