from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Like, Attendance
from .serializers import LikeSerializer, AttendanceSerializer
from rest_framework import generics, permissions, filters
from we_love_vinyls.permissions import IsMemberOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

class AllLikes(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    filter_backends = [
        filters.SearchFilter,DjangoFilterBackend,
    ]
    filterset_fields = [
        'member__id',
    ]
    
    def perform_create(self, serializer):
        serializer.save(member=self.request.user)

class OneLike(generics.RetrieveDestroyAPIView):
   
    permission_classes = [IsMemberOrReadOnly]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer



class AllAttendance(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all()

    filter_backends = [
        filters.SearchFilter,DjangoFilterBackend,
    ]
    filterset_fields = [
        'member__id',
    ]
    
    def perform_create(self, serializer):
        serializer.save(member=self.request.user)


class OneAttendance(generics.RetrieveDestroyAPIView):
   
    permission_classes = [IsMemberOrReadOnly]
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer