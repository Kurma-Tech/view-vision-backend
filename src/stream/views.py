from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import StreamSerializer

from .models import StreamDevice



# class StreamView(APIView):
#     def post(self, request):
#         serializer = StreamSerializer(data=request.data)
#         if serializer.is_valid():
#             stream = serializer.save()
#             StreamUserDevice.objects.create(userDevice=request.user, stream=stream)
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
            
    