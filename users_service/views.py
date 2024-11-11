from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import date, timedelta
from tasks_service.models import Task
from notifications_service.models import Notification
from tasks_service.serializers import TaskSerializer
from notifications_service.serializers import NotificationSerializer
from .models import User
from .serializers import UserRegisterSerializer, UserSerializer, CustomTokenObtainPairSerializer

class UserRegisterView(generics.CreateAPIView):
    """
    View for user registration. Allows unauthenticated registration for regular users.
    Admin registration requires authenticated admin role.
    """
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    
    def perform_create(self, serializer):
        # Check if the role is set to "admin" in the request data
        if self.request.data.get("role") == "admin":
            # Require admin authentication for registering an admin user
            if not self.request.user.is_authenticated or self.request.user.role != 'admin':
                raise PermissionDenied("Admin registration requires admin authentication.")
        
        # Save the user as per provided role (default to "user" if not specified)
        serializer.save()
    
class UserDetailView(generics.RetrieveAPIView):
    """
    Views for retrieving the details of authenticated user
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom view for obtaining JWT token with additional user info in response
    """
    serializer_class = CustomTokenObtainPairSerializer

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        # 1. Fetch tasks assigned to the user
        tasks = Task.objects.filter(assigned_to=user)

        # 2. Check if each task's due date is within a day
        today = date.today()
        tasks_data = []
        for task in tasks:
            task_data = TaskSerializer(task).data
            task_data['task_due'] = task.due_date and today < task.due_date <= (today + timedelta(days=1))
            tasks_data.append(task_data)

        # 3. Fetch unread notifications for the user
        notifications = Notification.objects.filter(user=user, is_read=False)
        notifications_data = NotificationSerializer(notifications, many=True).data

        # 4. Structure the response data
        response_data = {
            "tasks": tasks_data,
            "notifications": notifications_data,
            "unread_notifications_count": notifications.count(),
            "tasks_due_soon_count": sum(1 for task in tasks_data if task['task_due'])
        }

        return Response(response_data)
