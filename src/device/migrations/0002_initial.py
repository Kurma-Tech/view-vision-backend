# Generated by Django 4.1 on 2022-08-16 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdevice',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='device',
            name='deviceType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device.devicetype'),
        ),
        migrations.AddField(
            model_name='device',
            name='user',
            field=models.ManyToManyField(through='device.UserDevice', to=settings.AUTH_USER_MODEL),
        ),
    ]