from rest_framework import serializers

from .models import DeviceType, Server, Device


class DeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=DeviceType
        fields='__all__'

class DeviceSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Device
        fields=["channel_number","device_name","id"]
        
    def create(self, validated_data):
        return Device.objects.create(**validated_data)
      

class ServerSerializer(serializers.ModelSerializer):
    # device  = DeviceSerializer(many=True, read_only=True)
    deviceType_id = serializers.IntegerField()
    class Meta:
        model=Server
        exclude=("device","deviceType","user")

    def create(self, validated_data):
        return Server.objects.create(**validated_data)
        
          
class StreamServerSerializer(serializers.ModelSerializer):
    channel = serializers.SerializerMethodField()
    username = serializers.CharField(source="userName")
    class Meta:
        model = Server
        fields = ["port", "address", "username", "password", "channel"]
        
    def get_channel(self, obj):
        return "102"
    
   
  