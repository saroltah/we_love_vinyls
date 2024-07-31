from rest_framework import serializers
from .models import Record
from likes.models import Like
from comments.models import Comment
from django.contrib.humanize.templatetags.humanize import naturaltime


class RecordSerializer(serializers.ModelSerializer):
    advertiser = serializers.ReadOnlyField(source='advertiser.username')
    advertiser_id = serializers.ReadOnlyField(source='advertiser.profile.id')
    is_advertiser = serializers.SerializerMethodField()
    members_liking_count = serializers.ReadOnlyField()
    comment_count = serializers.ReadOnlyField()
    created = serializers.SerializerMethodField()

    def get_created(self, obj):
        return naturaltime(obj.created)

    def validate_image(self, value):
        if value.size > 2097152:
            raise serializers.ValidationError(
                'The image can not be larger than 2MB!'
                )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'The image height can not be larger than 4096px!'
                )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'The image width can not be larger than 4096px!'
                )
        return value

    def get_is_advertiser(self, obj):
        request = self.context['request']
        return request.user == obj.advertiser

    class Meta:
        model = Record
        fields = [
            'id', 'advertiser', 'artist', 'title', 'track_list',
            'created', 'condition', 'image', 'released', 'genre',
            'is_advertiser', 'members_liking_count', 'comment_count',
            'price', 'location', 'contact', 'advertiser_id',
        ]
