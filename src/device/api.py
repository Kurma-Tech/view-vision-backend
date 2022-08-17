from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response 


import requests
# import json


from .models import Device
from .serializers import DeviceSerializer


from ..stream.serializers import StreamSerializer
from src.stream.models import Stream, StreamDevice, StreamUser


class StreamAPI(APIView):
    def post(self, request, id):
        try:
            device = Device.objects.get(id=id,user=request.user)
            serializer = DeviceSerializer(device)
            payload_dict = serializer.data
            r = requests.post("https://httpbin.org/post", data=payload_dict)
            if (r.status_code==200):
                # responseData = json.loads(r.text)
                stream = Stream.objects.create(url=r.url, status=r.status_code)
                StreamDevice.objects.create(stream=stream, device=device)
                StreamUser.objects.create(stream=stream, user=request.user)
                serializer_stream = StreamSerializer(stream)
                return Response(serializer_stream.data)         
        except Device.DoesNotExist:
             return Response({"error": True, "info":"No data found"})
        except:
            return Response({"error": True, "info":"Server Error"})
   
   
