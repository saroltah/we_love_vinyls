from rest_framework import serializers
from .models import Profile
from likes.models import Like
from likes.models import Attendance
from django.contrib.humanize.templatetags.humanize import naturaltime

class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='member.id')
    member = serializers.ReadOnlyField(source='member.username')
    is_member = serializers.SerializerMethodField()
    liked_record_count = serializers.ReadOnlyField()
    attended_market_count = serializers.ReadOnlyField()
    created = serializers.SerializerMethodField()


    def get_created(self, obj):
        return naturaltime(obj.created)
   


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

    def get_is_member(self, obj):
        request = self.context['request']
        return request.user == obj.member

    class Meta:
        model = Profile
        fields = 'id', 'member', 'username', 'slug', 'preferred_music', 'about_me', 'created', 'image', 'is_member', 'liked_record_count', 'attended_market_count',  
