from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = [
            'user', 'username', 'slug', 'preferred_music', 'about_me', 'created_on', 'image'
        ]
