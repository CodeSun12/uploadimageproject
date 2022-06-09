from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ProfileSerializer
from rest_framework import serializers
from rest_framework.response import Response
from .models import Profile


# Create your views here.
class ProfileApiView(APIView):
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Done'})
        return Response(serializer.errors)

    def get(self, request):
        data = Profile.objects.all()
        serializer = ProfileSerializer(data, many=True)
        return Response(serializer.data)
