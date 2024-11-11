from rest_framework import serializers
from .models import Task
from users_service.models import User

class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='email',
        required=False, allow_null=True)
    
    class Meta:
        model = Task
        fields = ['id','title','description','status','due_date','assigned_to','created_at','updated_at']
        read_only_fields = ['created_at','updated_at']
