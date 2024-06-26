from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Like, Attendance
from .serializers import LikeSerializer, AttendanceSerializer
from rest_framework import generics, permissions
from we_love_vinyls.permissions import IsMemberOrReadOnly

class AllLikes(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OneLike(generics.RetrieveDestroyAPIView):
   
    permission_classes = [IsMemberOrReadOnly]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer



class AllAttendance(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OneAttendance(generics.RetrieveDestroyAPIView):
   
    permission_classes = [IsMemberOrReadOnly]
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer