from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='user.id')
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = '__all__' 
