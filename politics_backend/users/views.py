from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
User = get_user_model()
from .serializers import UserSerializer, UserRegistrationSerializer, UserApprovalSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

def get_current_user_from_session(request):
    """Get current user from session (no JWT)"""
    user_id = request.session.get('user_id')
    if user_id:
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
    return None

def require_admin(func):
    """Decorator to require admin privileges (session-based)"""
    def wrapper(request, *args, **kwargs):
        user = get_current_user_from_session(request)
        if not user:
            return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
        if not user.is_admin and not user.is_superuser:
            return Response({'error': 'Admin privileges required'}, status=status.HTTP_403_FORBIDDEN)
        return func(request, user, *args, **kwargs)
    return wrapper

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register_user(request):
    """User registration endpoint"""
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            'message': 'User registered successfully. Please wait for approval.',
            'user': UserSerializer(user).data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_user(request):
    """User login endpoint - Session based, no JWT tokens"""
    email = request.data.get('email')
    password = request.data.get('password')
    
    if not email or not password:
        return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = authenticate(request, username=email, password=password)
    
    if user is not None:
        if not user.is_approved:
            return Response({
                'error': 'Account not approved yet. Please contact admin for approval.'
            }, status=status.HTTP_403_FORBIDDEN)
        
        # Set session-based authentication (no JWT)
        request.session['user_id'] = user.id
        request.session['user_email'] = user.email
        
        return Response({
            'message': 'Login successful',
            'user': UserSerializer(user).data,
            'note': 'Session-based authentication - no JWT tokens'
        })
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def get_user_profile(request):
    """Get current user profile"""
    user = get_current_user_from_session(request)
    if user:
        return Response({
            'message': 'User profile retrieved successfully',
            'user': UserSerializer(user).data,
            'note': 'Session-based authentication working'
        })
    else:
        return Response({
            'message': 'No user logged in',
            'note': 'Please login to view profile'
        })

@api_view(['POST'])
@require_admin
def approve_user(request, user, user_id):
    """Approve a user (Admin only) - Session based, no JWT"""
    # Only superusers can approve users and make them admins
    if not user.is_superuser:
        return Response({
            'error': 'Only superusers can approve users'
        }, status=status.HTTP_403_FORBIDDEN)
    
    try:
        target_user = User.objects.get(id=user_id)
        target_user.approve_user(approved_by=user)
        return Response({
            'message': f'User {target_user.email} has been approved and made admin',
            'user': UserSerializer(target_user).data
        })
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@require_admin
def get_pending_users(request, user):
    """Get list of users waiting for approval (Admin only) - Session based, no JWT"""
    # Only superusers and admins can view pending users
    if not user.can_approve_users():
        return Response({
            'error': 'Only superusers and admins can view pending users'
        }, status=status.HTTP_403_FORBIDDEN)
    
    pending_users = User.objects.filter(is_approved=False)
    serializer = UserSerializer(pending_users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def protected_endpoint(request):
    """Example protected endpoint that only approved users can access"""
    # For now, just return a simple response without authentication
    return Response({
        'message': 'Welcome to the protected area!',
        'note': 'Authentication removed - no JWT tokens required'
    })
