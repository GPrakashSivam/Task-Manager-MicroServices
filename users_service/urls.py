from django.urls import path
from .views import UserRegisterView, UserDetailView, CustomTokenObtainPairView, DashboardView

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('me/',UserDetailView.as_view(),name='user_detail'),
    path('login/',CustomTokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('dashboard/',DashboardView.as_view(),name='dashboard')
]