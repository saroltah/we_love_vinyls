from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Record
from .serializers import RecordSerializer
from django.http import Http404


class AllRecords(APIView):
    def get(self, request):
        records = Record.objects.all()
        serializer = RecordSerializer(records, many= True)
        return Response(serializer.data)

class OneRecord(APIView):
    serializer_class = RecordSerializer

    def get_object(self, pk):
        try:
            record=Record.objects.get(pk=pk)
            return record
        except Record.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        record = self.get_object(pk)
        serializer=RecordSerializer(record)
        return Response(serializer.data)

    def put (self, request, pk):
        record =self.get_object(pk)
        serializer=RecordSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

