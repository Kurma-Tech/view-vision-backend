from django.db import models


from src.device.models import Server
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
    user = models.ManyToManyField(User, through="StreamUser")
    server= models.ManyToManyField(Server, through="StreamServer")
    
    def __str__(self):
        return self.url
   
    
class StreamServer(models.Model):
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.server.serverName} - {self.stream.url}"
    

class StreamUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.email} - {self.stream.url}"