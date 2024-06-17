from rest_framework import serializers
from .models import Market

class MarketSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source='organizer.username')

    class Meta:
        model = Market
        fields = [
            'id', 'organizer', 'country', 'city', 'address', 'date', 'time', 'description',
        ]
