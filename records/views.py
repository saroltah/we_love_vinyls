from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Record
from .serializers import RecordSerializer
from django.http import Http404
from rest_framework import status, permissions, generics, filters
from we_love_vinyls.permissions import IsAdvertiserOrReadOnly
from django.db.models import Count
import django_filters
from django_filters.rest_framework import (
    DjangoFilterBackend,
    FilterSet,
    CharFilter,
)


class RecordFilter(django_filters.FilterSet):
    genre = django_filters.CharFilter(
        field_name='genre', lookup_expr='icontains')
    member = django_filters.CharFilter(
        field_name='like__member__id', lookup_expr='icontains')
    advertiser = django_filters.CharFilter(
        field_name='advertiser__id', lookup_expr='icontains')

    class Meta:
        model = Record
        fields = ['genre', 'advertiser', 'member']


class AllRecords(generics.ListCreateAPIView):
    queryset = Record.objects.annotate(
        members_liking_count=Count('like', distinct=True),
        comment_count=Count('comment', distinct=True),)

    filter_backends = [
        filters.SearchFilter, DjangoFilterBackend,
    ]

    filterset_class = RecordFilter

    search_fields = [
        'artist',
        'title',
    ]
    serializer_class = RecordSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(advertiser=self.request.user)


class OneRecord(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecordSerializer
    permission_classes = [IsAdvertiserOrReadOnly]

    queryset = Record.objects.annotate(
        members_liking_count=Count('like', distinct=True),
        comment_count=Count('comment', distinct=True),
        ).order_by('-created')
