from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status

import requests
import json

from src.device.models import Server
from src.device.serializers import StreamServerSerializer

from .serializers import StreamSerializer
from .models import Stream, StreamServer, StreamUser


class StreamAPI(APIView):
    def post(self, request, id):
        try:
            server = Server.objects.get(id=id,user=request.user)
            serializer = StreamServerSerializer(server)
            payload_dict = serializer.data
            breakpoint()
            print(payload_dict)
            r = requests.post("http://139.162.230.224/test", data=payload_dict)
            if (r.status_code==200):
                stream = Stream.objects.create(url=json.loads(r.text)["data"]["streamUrl"], status="active")
                StreamServer.objects.create(stream=stream, server=server)
                StreamUser.objects.create(stream=stream, user=request.user)
                serializer_stream = StreamSerializer(stream)
                return Response(serializer_stream.data, status=status.HTTP_200_OK) 
            else:
                return Response({"error": True, "info":"Bad Request"}, status=status.HTTP_400_BAD_REQUEST)
        except Server.DoesNotExist:
            return Response({"error": True, "info":"No data found"}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"error": True, "info":"Stream start failed."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   
   
