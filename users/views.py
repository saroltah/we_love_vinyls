from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from django.http import Http404
from rest_framework import status
from we_love_vinyls.permissions import IsOwnerOrReadOnly


class AllProfiles(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True, context = {'request' : request})
        return Response(serializer.data)

class OneProfile(APIView):
    serializer_class = ProfileSerializer
    permission_classes =[IsOwnerOrReadOnly]

    def get_object(self, slug):
        try:
            profile=Profile.objects.get(slug=slug)
            self.check_object_permissions (self.request, profile)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, slug):
        profile = self.get_object(slug)
        serializer=ProfileSerializer(profile, context = {'request' : request})
        return Response(serializer.data)

    def put (self, request, slug):
        profile =self.get_object(slug)
        serializer=ProfileSerializer(profile, data=request.data, context = {'request' : request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
