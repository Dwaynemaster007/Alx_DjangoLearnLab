from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source='actor.username')
    post_title = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Notification
        fields = ['id', 'actor', 'verb', 'post', 'post_title', 'read', 'timestamp']
