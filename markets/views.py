from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Market
from .serializers import MarketSerializer
from django.http import Http404
from rest_framework import status


class AllMarkets(APIView):
    def get(self, request):
        markets = Market.objects.all()
        serializer = MarketSerializer(markets, many= True)
        return Response(serializer.data)

class OneMarket(APIView):
    serializer_class = MarketSerializer

    def get_object(self, pk):
        try:
            market=Market.objects.get(pk=pk)
            return market
        except Market.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        market = self.get_object(pk)
        serializer=MarketSerializer(market)
        return Response(serializer.data)

    def put (self, request, pk):
        market =self.get_object(pk)
        serializer=MarketSerializer(market, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
