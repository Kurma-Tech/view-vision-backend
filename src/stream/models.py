from django.db import models


from src.device.models import Device
from src.user.models import User


class Stream(models.Model):
    url = models.TextField(max_length=200)
    
    class StreamStatusChoice(models.TextChoices):
        ACTIVE = ("active")
        INACTIVE = ("inactive")
        DISABLED = ("disabled")
        NO_CONNECTION = ("no_connection")
        
    status = models.CharField(
        max_length=200,
        choices=StreamStatusChoice.choices,
        default=StreamStatusChoice.INACTIVE,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.url
   
    
class StreamDevice(models.Model):
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.stream.url} - {self.device.deviceName}"
    

class StreamDeviceUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    streamDevice = models.ForeignKey(StreamDevice, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} - {self.streamDevice.stream.url}"