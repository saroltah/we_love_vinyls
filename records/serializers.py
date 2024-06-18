from rest_framework import serializers
from .models import Record

class RecordSerializer(serializers.ModelSerializer):
    advertiser = serializers.ReadOnlyField(source='advertiser.username')
    is_advertiser = serializers.SerializerMethodField()

    def get_is_advertiser(self, obj):
        request = self.context['request']
        return request.user == obj.advertiser

    class Meta:
        model = Record
        fields = [
            'id', 'advertiser', 'artist', 'title', 'track_list', 'created_on', 'condition', 'image', 'released', 'is_advertiser',
        ]
