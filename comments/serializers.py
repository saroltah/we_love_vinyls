from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    member = serializers.ReadOnlyField(source='member.username')
    is_member = serializers.SerializerMethodField()
    member_id = serializers.ReadOnlyField(source='member.profile.id')
    member_image = serializers.ReadOnlyField(source='member.profile.image.url')

    def get_is_member(self, obj):
        request = self.context['request']
        return request.user == obj.member

    class Meta:
        model = Comment
        fields = [
            'id', 'member', 'content', 'commented_record', 'created_on', 'is_member', 'member_id', 'member_image'
        ]

class OneCommentSerializer(CommentSerializer):

    commented_record = serializers.ReadOnlyField(source='commented_record.id')