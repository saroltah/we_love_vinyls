from rest_framework import serializers
from .models import Profile
from likes.models import Like

class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='member.id')
    member = serializers.ReadOnlyField(source='member.username')
    is_member = serializers.SerializerMethodField()
    liked_record_count = serializers.ReadOnlyField()
    liked_record_id = serializers.SerializerMethodField()
    attended_market_count = serializers.ReadOnlyField()
    


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

    def get_liked_record_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            liked_record = Like.objects.filter(
                member=user, liked_record =obj.id
            ).first()
            return liked_record.id if liked_record else None
        return None
    
    class Meta:
        model = Profile
        fields = 'id', 'member', 'username', 'slug', 'preferred_music', 'about_me', 'created_on', 'image', 'is_member', 'liked_record_count', 'liked_record_id', 'attended_market_count',  
