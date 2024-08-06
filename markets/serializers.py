from rest_framework import serializers
from .models import Market
from likes.models import Attendance


class MarketSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source='organizer.username')
    organizer_id = serializers.ReadOnlyField(source='organizer.profile.id')
    is_organizer = serializers.SerializerMethodField()
    members_attending_count = serializers.ReadOnlyField()
    organizer_image = serializers.ReadOnlyField(source='organizer.profile.image.url')
    start = serializers.TimeField(format='%H:%M')
    end = serializers.TimeField(format='%H:%M')
    attendance_id = serializers.SerializerMethodField()

    

    def get_is_organizer(self, obj):
        request = self.context['request']
        return request.user == obj.organizer

    def get_attendance_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            attendance = Attendance.objects.filter(
                member=user, attended_market=obj
            ).first()
            return attendance.id if attendance else None
        return None

    class Meta:
        model = Market
        fields = [
            'id', 'organizer', 'country', 'city', 'address', 'date',
            'start', 'end', 'description', 'is_organizer',
            'members_attending_count', 'organizer_id', 'organizer_image','attendance_id'
            ]
