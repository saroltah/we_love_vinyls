from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from django.http import Http404
from rest_framework import status


class AllProfiles(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many= True)
        return Response(serializer.data)

class OneProfile(APIView):
    serializer_class = ProfileSerializer

    def get_object(self, slug):
        try:
            profile=Profile.objects.get(slug=slug)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, slug):
        profile = self.get_object(slug)
        serializer=ProfileSerializer(profile)
        return Response(serializer.data)

    def put (self, request, slug):
        profile =self.get_object(slug)
        serializer=ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
