from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='member.id')
    member = serializers.ReadOnlyField(source='member.username')
    is_member = serializers.SerializerMethodField()

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
        fields = '__all__' 
