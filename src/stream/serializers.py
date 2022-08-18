from rest_framework import serializers

from .models import StreamDevice, Stream, StreamUser

class StreamDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamDevice
        fields='__all__'
        
              
              
class StreamUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=StreamUser
        fields='__all__'


class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream 
        fields = "__all__"
         
    def create(self, validated_data):
        return Stream.objects.create(**validated_data)
        
        
        

    
        
    
        