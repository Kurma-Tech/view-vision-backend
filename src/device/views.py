from ctypes import addressof
from http import server
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Server, UserServer, Device
from .serializers import DeviceSerializer, ServerSerializer

import json 

class ServerView(APIView, IsAuthenticated):
    serializer_class = ServerSerializer

    def get(self, request):
        currentUser = request.user
        server = Server.objects.all()
        serializer = ServerSerializer(server, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        server_name = request.data.get('server_name')
        device = request.data.get('device')
        device_list = Device.objects.filter(id__in=server)
        serializer = ServerSerializer(data=request.data)
        
        if serializer.is_valid():
            server = serializer.save()
            UserServer.objects.create(user=request.user, server=server)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            server = Server.objects.get(id=id,user=request.user)
            print(server)
            serializer = ServerSerializer(server, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Server.DoesNotExist:
            return Response({"error": True, "info":"No data found"})
        except:
            return Response({"error": True, "info":"Server Error"})

    def delete(self, request, id, format=None):
        server = Server.objects.filter(id=id,user=request.user)
        if len(server) > 0:
            server.delete()
        else:
            return Response({"error":True, "info":"you cannot delete the other server"})
        return Response({"error":False, "info":"Server deleted"},status=status.HTTP_204_NO_CONTENT) 
       
       
class DeviceChannel(APIView, IsAuthenticated):
    serializer=DeviceSerializer
     
    def get(self, request):
        currentUser = request.user
        devices= Device.objects.filter(user=request.user)
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

    
    def post(self, request, **kwargs):
        # address = request.data.get("address")
        device = request.data.get("device")
        
        # devices = Device.objects.filter(id__in=device)
        # instance = Server.objects.create(address=address)
        
        # for device in devices:
        #     instance.device.add(device)
        
            
        serializer = DeviceSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(user=self.request.user)   
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, id):
        try:
            device = Device.objects.get(id=id, user=request.user)
            serializer = DeviceSerializer(device, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Device.DoesNotExist:
            return Response({"error":True, "info":"No data found"})
        except:
            return Response({"error":True, "info":"Server Error"})
        
        
    def delete(self, request, id):
        device = Device.objects.filter(id=id, user=request.user)
        if len(device)>0:
            device.delete()
        else:
            return Response({"error":True, "info":"You cannot delete other device channel"})
        return Response({"error":True, "info":"device deleted"}, status=status.HTTP_204_NO_CONTENT)
    
    
    def filter(self, request):
        device = Device.objects.filter(channel_name=request.data.get("channel_name"))
        serializer = DeviceSerializer(device, many=True)
        return Response(serializer.data)
        
        

    
class ChannelsView(APIView, IsAuthenticated): 
    
    serializer_class = ServerSerializer()
    
    def get(self, request):
        channels = Server.objects.filter(address=request.data.get("address"))
        print(channels)
        
        # channels = Server.objects.filter(id=request.data.get("id")).values("channels")
        # serializer = ServerSerializer(, )

        
        
    
      
        
    