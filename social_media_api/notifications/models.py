from django.conf import settings
from django.db import models


class Notification(models.Model):
    """Tells a user that someone interacted with them (e.g. liked or commented on their post)."""

    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notifications', on_delete=models.CASCADE)
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='actor_notifications', on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    post = models.ForeignKey('posts.Post', null=True, blank=True, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.actor} {self.verb} -> {self.recipient}'
