from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Record
from .serializers import RecordSerializer


class AllRecords(APIView):
    def get(self, request):
        records = Record.objects.all()
        serializer = RecordSerializer(records, many= True)
        return Response(serializer.data)

