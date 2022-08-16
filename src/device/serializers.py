from rest_framework import serializers

from .models import Device, DeviceType


class DeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=DeviceType
        fields='__all__'
    
class DeviceSerializer(serializers.ModelSerializer):
    deviceType_id = serializers.IntegerField()
    class Meta:
        model = Device
        fields = ["port", "address", "deviceName", "userName", "password", "deviceType_id","id"]

    def create(self, validated_data):
        return Device.objects.create(**validated_data)