from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Market
from .serializers import MarketSerializer
from django.http import Http404
from rest_framework import status, permissions, generics, filters
from we_love_vinyls.permissions import IsOrganizerOrReadOnly
from django.db.models import Count
import django_filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter



class MarketFilter(django_filters.FilterSet):
    member = django_filters.CharFilter(field_name='attendance__member__id', lookup_expr='icontains')
    organizer = django_filters.CharFilter(field_name='attendance__organizer__id', lookup_expr='icontains')

    class Meta:
        model = Market
        fields = ['organizer', 'member']

class AllMarkets(generics.ListCreateAPIView):
    queryset = Market.objects.annotate(
        members_attending_count=Count('attendance', distinct=True),
    ).order_by('-created')
    filter_backends = [
        filters.SearchFilter, DjangoFilterBackend,
    ]
    filterset_class = MarketFilter
    search_fields = [
        'country',
        'city',
    ]
    serializer_class = MarketSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class OneMarket(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MarketSerializer
    permission_classes = [IsOrganizerOrReadOnly]
    queryset = Market.objects.annotate(
        members_attending_count=Count('attendance', distinct=True),
    ).order_by('-created')
