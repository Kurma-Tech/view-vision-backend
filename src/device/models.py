from django.db import models

from src.user.models import User

class DeviceType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Device(models.Model):
    deviceType = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    port = models.CharField(max_length=255, null=True, blank=True) 
    address = models.TextField(null=True, blank=True) 
    deviceName = models.CharField(max_length=255, null=True, blank=True)
    userName = models.CharField(max_length=255, default='admin')
    password = models.CharField(max_length=255)
    user = models.ManyToManyField(User, through="UserDevice")

    def __str__(self):
        return f"{self.deviceName} - {self.userName}"

class UserDevice(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email} - {self.device.deviceName}"

    