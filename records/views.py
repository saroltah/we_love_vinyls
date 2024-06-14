from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Record

class AllRecords(APIView):
    def get(self, request):
        records = Record.objects.all()
        return Response(records)

