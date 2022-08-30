from django.db import models

from src.user.models import User


class DeviceType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Server(models.Model):
    device_type= models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    port = models.CharField(max_length=255, null=True, blank=True) 
    address = models.TextField(null=True, blank=True) 
    server_name = models.CharField(max_length=255, null=True, blank=True)
    user_name = models.CharField(max_length=255, default='admin')
    password = models.CharField(max_length=255)
    user = models.ManyToManyField(User, through="UserServer")
    device = models.ManyToManyField("Device")
    
    def combined_fields(self):
        return f"{self.user_name} - {self.address} - {self.server_name}"
    
    def __str__(self):
        return f"{self.server_name}"
    

class UserServer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email} - {self.server.server_name}"


class Device(models.Model):
    channel_number = models.PositiveIntegerField(null=True, blank=True)
    device_name = models.CharField(max_length=100,blank=True, null=True) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.device_name} - {self.channel_number}"
  
    