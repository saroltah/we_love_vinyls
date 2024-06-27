from rest_framework import serializers
from .models import Record
from likes.models import Like

class RecordSerializer(serializers.ModelSerializer):
    advertiser = serializers.ReadOnlyField(source='advertiser.username')
    is_advertiser = serializers.SerializerMethodField()
    like_sent_id = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 2097152:
            raise serializers.ValidationError('The image can not be larger than 2MB!')
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

    def get_like_sent_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like_sent = Like.objects.filter(
                member=user, liked_record =obj.id
            ).first()
            return like_sent.id if like_sent else None
        return None


    class Meta:
        model = Record
        fields = [
            'id', 'advertiser', 'artist', 'title', 'track_list', 'created_on', 'condition', 'image', 'released', 'is_advertiser', 'like_sent_id'
        ]
