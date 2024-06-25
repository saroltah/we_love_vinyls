from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Record
from .serializers import RecordSerializer
from django.http import Http404
from rest_framework import status, permissions
from we_love_vinyls.permissions import IsAdvertiserOrReadOnly


class AllRecords(APIView):

    serializer_class = RecordSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        records = Record.objects.all()
        serializer = RecordSerializer(records, many= True, context = {'request' : request})
        return Response(serializer.data)

    def post (self, request, pk):
        record =self.get_object(pk)
        serializer=RecordSerializer(record, data=request.data, context = {'request' : request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OneRecord(APIView):
    serializer_class = RecordSerializer
    permission_classes =[IsAdvertiserOrReadOnly]

    def get_object(self, pk):
        try:
            record=Record.objects.get(pk=pk)
            return record
        except Record.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        record = self.get_object(pk)
        serializer=RecordSerializer(record, context = {'request' : request})
        return Response(serializer.data)

    def put (self, request, pk):
        record =self.get_object(pk)
        serializer=RecordSerializer(record, data=request.data, context = {'request' : request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

