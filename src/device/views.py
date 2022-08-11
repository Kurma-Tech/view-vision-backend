from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Device, UserDevice 
from .serializers import DeviceSerializer


class DeviceView(APIView, IsAuthenticated):
    serializer_class = DeviceSerializer

    def get(self, request):
        currentUser = request.user
        devices = Device.objects.filter(user=currentUser)
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            device = serializer.save()
            UserDevice.objects.create(user=request.user, device=device)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        try:
            device = Device.objects.get(id=id,user=request.user)
            print(device)
            serializer = DeviceSerializer(device, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Device.DoesNotExist:
            return Response({"error": True, "info":"No data found"})
        except:
            return Response({"error": True, "info":"Server Error"})

    def delete(self, request, id, format=None):
        device = Device.objects.filter(id=id,user=request.user)
        if len(device) > 0:
            device.delete()
        else:
            return Response({"error":True, "info":"you cannot delete the other devices"})
        return Response({"error":False, "info":"Device deleted"},status=status.HTTP_204_NO_CONTENT) 
       
