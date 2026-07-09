from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer
# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer = RegisterSerializer(data=request.data)

        print(serializer.is_valid())
        print(serializer.errors)

        serializer.is_valid(raise_exception=True)
        serializer = RegisterSerializer(data=request.data)
        serializer.save()
        return Response({'message':'User created successfully'},status=status.HTTP_201_CREATED)