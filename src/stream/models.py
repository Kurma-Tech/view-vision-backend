from django.db import models

from src.device.models import Device
# from src.user.models import 


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
    device = models.ManyToManyField(Device, through="StreamDevice")
    
class StreamDevice(models.Model):
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.stream.url} - {self.device.deviceName}"
