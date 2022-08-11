from rest_framework import serializers

from .models import StreamDevice, Stream 

class StreamDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamDevice
              

class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream 
        fields = "__all__"
        
        
    def create(self, validated_data):
        return Stream.objects.create(**validated_data)
        
        
        

     
        
    
        