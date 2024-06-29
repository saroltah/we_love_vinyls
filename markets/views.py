from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Market
from .serializers import MarketSerializer
from django.http import Http404
from rest_framework import status, permissions, generics
from we_love_vinyls.permissions import IsOrganizerOrReadOnly
from django.db.models import Count

class AllMarkets(generics.ListCreateAPIView):
    queryset=Market.objects.annotate(
        members_attending_count=Count('attendance', distinct=True),
    ).order_by('-created_on')
    serializer_class = MarketSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

class OneMarket(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MarketSerializer
    permission_classes =[IsOrganizerOrReadOnly]

    queryset = Market.objects.annotate(
        members_attending_count=Count('attendance', distinct=True),
    ).order_by('-created_on')
