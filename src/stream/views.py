from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import StreamSerializer

from .models import Stream

   
class StreamView(APIView):
    def get(self, request):
        currentUser = request.user
        streams = Stream.objects.filter(user=currentUser)
        serializer = StreamSerializer(streams, many=True)
        return Response(serializer.data)
    
    def delete(self, request, id):
        stream = Stream.objects.filter(id=id,user=request.user)
        if len(stream)>0:
            stream.delete()
        else:
            return Response({"Error":True, "Info":"Stream could not be found" })
        return Response({"Error":False, "Info":"Stream Deleted"},status=status.HTTP_204_NO_CONTENT)
            

        
        
        