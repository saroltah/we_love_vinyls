from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Record
from .serializers import RecordSerializer
from django.http import Http404
from rest_framework import status, permissions, generics
from we_love_vinyls.permissions import IsAdvertiserOrReadOnly
from django.db.models import Count


class AllRecords(generics.ListCreateAPIView):
    queryset = Record.objects.all() 
    serializer_class = RecordSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(advertiser=self.request.user)

class OneRecord(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecordSerializer
    permission_classes =[IsAdvertiserOrReadOnly]

    queryset = Record.objects.annotate(
        members_liking_count=Count('like__member', distinct=True),
        comment_count=Count('comment__content', distinct=True),
    ).order_by('-created_on')