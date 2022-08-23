from rest_framework import serializers


from .models import StreamServer, Stream, StreamUser


class StreamServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamServer
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
        
        


    
        
    
        