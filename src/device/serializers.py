from rest_framework import serializers


from .models import DeviceType, Server, Device, Provider


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
    device_type_id = serializers.IntegerField()
    
    class Meta:
        model=Server
        exclude=("device","user","device_type")
    
    def create(self, validated_data):
        print(validated_data)
        # providerQuery = Provider.objects.filter(id=dict(validated_data)["provider"])
        # if (providerQuery.exists()):
        # provider = providerQuery.first()
        validated_data["rtsp_port"] = validated_data["provider"].rtsp_port
        validated_data["http_port"] = validated_data["provider"].http_port
        return Server.objects.create(**validated_data)
        
          
class StreamServerSerializer(serializers.ModelSerializer):
    channel = serializers.SerializerMethodField()
    class Meta:
        model = Server
        fields = ["port", "address", "user_name", "password", "channel"]
        
    def get_channel(self, obj):
        return "102"
    
class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ("id", "rtsp_port","http_port")
    
   
  