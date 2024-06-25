from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Market
from .serializers import MarketSerializer
from django.http import Http404
from rest_framework import status, permissions
from we_love_vinyls.permissions import IsOrganizerOrReadOnly


class AllMarkets(APIView):

    serializer_class = MarketSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        markets = Market.objects.all()
        serializer = MarketSerializer(markets, many= True, context = {'request' : request})
        return Response(serializer.data)

    def post (self, request, pk):
        market =self.get_object(pk)
        serializer=MarketSerializer(market, data=request.data, context = {'request' : request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OneMarket(APIView):
    serializer_class = MarketSerializer
    permission_classes =[IsOrganizerOrReadOnly]

    def get_object(self, pk):
        try:
            market=Market.objects.get(pk=pk)
            return market
        except Market.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        market = self.get_object(pk)
        serializer=MarketSerializer(market, context = {'request' : request})
        return Response(serializer.data)

    def put (self, request, pk):
        market =self.get_object(pk)
        serializer=MarketSerializer(market, data=request.data, context = {'request' : request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
