from rest_framework import serializers
from .models import Like, Attendance
from django.db import IntegrityError
from django.contrib.humanize.templatetags.humanize import naturaltime


class LikeSerializer(serializers.ModelSerializer):
    member = serializers.ReadOnlyField(source='member.username')
    is_member = serializers.SerializerMethodField()
    created = serializers.SerializerMethodField()
    member_id = serializers.ReadOnlyField(source='member.profile.id')
    

    def get_created(self, obj):
        return naturaltime(obj.created)

    def get_is_member(self, obj):
        request = self.context['request']
        return request.user == obj.member

    class Meta:
        model = Like
        fields = [
            'id', 'member', 'liked_record', 'created', 'is_member', 'member_id'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})


class AttendanceSerializer(serializers.ModelSerializer):
    member = serializers.ReadOnlyField(source='member.username')
    is_member = serializers.SerializerMethodField()

    def get_is_member(self, obj):
        request = self.context['request']
        return request.user == obj.member

    class Meta:
        model = Attendance
        fields = [
            'id', 'member', 'attended_market', 'created', 'is_member', 'member_id'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})
