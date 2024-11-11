from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from users_service.models import User
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    Viewset for managing Tasks. Admin can perform all CRUD actions, 
    while regular users can only view tasks assigned to them
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status','due_date']  #Enable filtering by status & due date
    ordering_fields = ['due_date','created_at']  #Allow ordering tasks by due date/created date

    def get_permissions(self):
        if self.action in ['create','destroy']:
            self.permission_classes = [permissions.IsAdminUser]
        else:
            self.permission_classes = [permissions.IsAuthenticated]

        return super().get_permissions()
    
    def get_queryset(self):
        user = self.request.user
        if user.role == 'user':
            return self.queryset.filter(assigned_to=user).order_by('due_date')

        return self.queryset.order_by('-due_date')
    
    def update(self, request, *args, **kwargs):
        """
        Allow admins to update tasks, including re-assigning them to other users
        Regular user can update their tasks status assigned to them
        """
        task = self.get_object()
        user = request.user
        print(f"User-{user}, Task-{task}")
        # Check if the user is a regular user and restrict them to updating only their assigned tasks
        if user.role == 'user' and task.assigned_to != user:
            return Response({"detail": "You don't have permission to update this task"},status=status.HTTP_403_FORBIDDEN)
        
        # If the user is a regular user, limit updates to the 'status' field only
        if user.role == 'user':
            if 'status' not in request.data:
                return Response({"detail": "You can only update status of this Task."},status=status.HTTP_400_BAD_REQUEST)
            
            # Filter request data to allow only the 'status' field
            request_data = {'status':request.data['status']}
        
        else: # update for admin user
            request_data = request.data # Admins can update all fields
            # check if assigned user is in request data
            if 'assigned_to' in request_data:
                assigned_user_email = request_data.get('assigned_to')
                try:
                    assigned_user = User.objects.get(email=assigned_user_email)
                    task.assigned_to = assigned_user #re-assign the task
                except User.DoesNotExist:
                    return Response({"error":"User with provided email does not exist."},status=status.HTTP_400_BAD_REQUEST)
            
        serializer = self.get_serializer(task, data=request_data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)