from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import NotificationSerializer


class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    """The signed-in user's notifications, newest first (unread ones first)."""

    serializer_class = NotificationSerializer

    def get_queryset(self):
        return self.request.user.notifications.select_related('actor', 'post').order_by('read', '-timestamp')

    @action(detail=False, methods=['post'])
    def mark_as_read(self, request):
        updated = self.get_queryset().filter(read=False).update(read=True)
        return Response({'status': 'notifications marked as read', 'updated': updated}, status=status.HTTP_200_OK)
