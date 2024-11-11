from rest_framework import viewsets, permissions
from .models import Notification
from .serializers import NotificationSerializer

class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Viewset for retreiving notifications. Only authenticated users can access
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        #only returns notifications for logged in user
        return Notification.objects.filter(user=self.request.user,is_read=False).order_by('-timestamp')