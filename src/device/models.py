from django.db import models


class DeviceType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Device(models.Model):
    deviceType = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    Port = models.CharField(max_length=255, null=True, blank=True) 
    Address = models.TextField(null=True, blank=True) 
    DeviceName = models.CharField(max_length=255, null=True, blank=True)
    UserName = models.CharField(max_length=255, default='admin')
    Password = models.CharField(max_length=255)

    def __str__(self):
        return self.Address
        

