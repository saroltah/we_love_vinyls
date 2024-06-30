from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from django.http import Http404
from rest_framework import generics, filters, status
from we_love_vinyls.permissions import IsMemberOrReadOnly
from django.db.models import Count



class AllProfiles(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class OneProfile(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes =[IsMemberOrReadOnly]
    lookup_field = 'slug'
    queryset = Profile.objects.annotate(
        liked_record_count=Count('member__like', distinct=True),
        attended_market_count=Count('member__attendance', distinct=True),
    ).order_by('-created')

