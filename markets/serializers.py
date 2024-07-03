from rest_framework import serializers
from .models import Market
from likes.models import Attendance


class MarketSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source='organizer.username')
    is_organizer = serializers.SerializerMethodField()
    members_attending_count = serializers.ReadOnlyField()

    def get_is_organizer(self, obj):
        request = self.context['request']
        return request.user == obj.organizer

    class Meta:
        model = Market
        fields = [
            'id', 'organizer', 'country', 'city', 'address', 'date',
            'start', 'end', 'description', 'is_organizer',
            'members_attending_count',
            ]
