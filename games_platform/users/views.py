import jwt
from django.conf import settings
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from rest_framework import exceptions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import CustomUser
from .serializers import CustomRegisterSerializer, CustomUserSerializer
from .utils import generate_access_token, generate_refresh_token


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    serialized_user = CustomUserSerializer(user).data
    return Response({'user': serialized_user })


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    serializer = CustomRegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if (username is None) or (password is None):
        raise exceptions.AuthenticationFailed('username and password required')
    user = CustomUser.objects.filter(username=username).first()
    if(user is None):
        raise exceptions.AuthenticationFailed('user not found')
    if (not user.check_password(password)):
        raise exceptions.AuthenticationFailed('wrong password')
    serialized_user = CustomUserSerializer(user).data
    access_token = generate_access_token(user)
    refresh_token = generate_refresh_token(user)
    response = Response()
    response.data = {
        'access_token': access_token,
        'refresh_token': refresh_token,
    }
    return response


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token_view(request):
    refresh_token = request.data.get('refresh_token')
    if refresh_token is None:
        raise exceptions.AuthenticationFailed(
            'Authentication credentials were not provided.')
    try:
        payload = jwt.decode(
            refresh_token, settings.REFRESH_TOKEN_SECRET, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed(
            'expired refresh token, please login again.')
    user = CustomUser.objects.filter(id=payload.get('user_id')).first()
    if user is None:
        raise exceptions.AuthenticationFailed('User not found')
    if not user.is_active:
        raise exceptions.AuthenticationFailed('user is inactive')
    access_token = generate_access_token(user)
    return Response({'access_token': access_token})



