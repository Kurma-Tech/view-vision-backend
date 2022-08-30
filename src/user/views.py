from django.shortcuts import render


from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import UserSerializer
from .models import User


class UserView(APIView):
    permission_classes = [IsAuthenticated]
    
    
    def get(self, request):
        # currentUser = request.user
        users = User.objects.filter()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)