from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status 

from .models import Business

from .serializers import RegistrationSerializer, BusinessUserRegistrationSerializer


User = get_user_model()

class RegistrationView(generics.CreateAPIView):
    model = User
    serializer_class = RegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            return Response(
                {
                    "access_token": str(
                        RefreshToken.for_user(user).access_token
                    )
                },
                status=201,
            )
            
class BusinessRegestrationView(generics.CreateAPIView):
    model = Business
    serializer_class = BusinessUserRegistrationSerializer
    permission_classes = (AllowAny,)
    
    def post(self, request):
        serializer = BusinessUserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
   
    