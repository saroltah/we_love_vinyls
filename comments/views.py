from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer, OneCommentSerializer
from rest_framework import generics, permissions, filters
from we_love_vinyls.permissions import IsMemberOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class AllComments(generics.ListCreateAPIView):

    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Comment.objects.all()

    filter_backends = [
        filters.SearchFilter,DjangoFilterBackend,
    ]
    filterset_fields = [
        'commented_record',
    ]

    def perform_create(self, serializer):
        serializer.save(member=self.request.user)

class OneComment(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = [IsMemberOrReadOnly]
    serializer_class = OneCommentSerializer
    queryset = Comment.objects.all()
