from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Record
from .serializers import RecordSerializer
from django.http import Http404
from rest_framework import status, permissions, generics, filters
from we_love_vinyls.permissions import IsAdvertiserOrReadOnly
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend


class AllRecords(generics.ListCreateAPIView):
    queryset = Record.objects.annotate(
        members_liking_count=Count('like', distinct=True),
        comment_count=Count('comment', distinct=True),)
    filter_backends = [
        filters.SearchFilter, DjangoFilterBackend,
    ]
    filterset_fields = [
        'genre',
    ]
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
