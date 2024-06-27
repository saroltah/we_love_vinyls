from rest_framework import serializers
from .models import Market
from likes.models import Attendance

class MarketSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source='organizer.username')
    is_organizer = serializers.SerializerMethodField()
    person_attending_id = serializers.SerializerMethodField()

    def get_is_organizer(self, obj):
        request = self.context['request']
        return request.user == obj.organizer

    def get_person_attending_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            person_attending = Attendance.objects.filter(
                member=user, attended_market =obj.id
            ).first()
            return person_attending.id if person_attending else None
        return None

    class Meta:
        model = Market
        fields = [
            'id', 'organizer', 'country', 'city', 'address', 'date', 'start', 'end', 'description', 'is_organizer', 'person_attending_id',
        ]
