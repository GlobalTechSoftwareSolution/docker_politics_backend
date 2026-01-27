from django.urls import path
from . import views

urlpatterns = [
    # Authentication endpoints
    path('api/register/', views.register_user, name='register'),
    path('api/login/', views.login_user, name='login'),
    path('api/profile/', views.get_user_profile, name='profile'),
    
    # Admin endpoints (for approval workflow)
    path('api/pending-users/', views.get_pending_users, name='pending_users'),
    path('api/approve-user/<int:user_id>/', views.approve_user, name='approve_user'),
    
    # Protected endpoint example
    path('api/protected/', views.protected_endpoint, name='protected'),
]