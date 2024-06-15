from rest_framework import serializers
from .models import Record

class RecordSerializer(serializers.ModelSerializer):
    uploader = serializers.ReadOnlyField(source='uploader.username')

    class Meta:
        model = Record
        fields = [
            'id', 'uploader', 'author', 'title', 'slug', 'track_list', 'created_on', 'condition', 'image', 'released',
        ]
