from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer, UserSerializer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    """POST username, email, password -> new user plus an auth token."""

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(APIView):
    """POST username and password -> auth token."""

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = authenticate(username=request.data.get('username'), password=request.data.get('password'))
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': UserSerializer(user).data})


class ProfileView(generics.RetrieveUpdateAPIView):
    """GET or PATCH the signed-in user's profile."""

    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class FollowUserView(generics.GenericAPIView):
    queryset = User.objects.all()

    def post(self, request, user_id):
        target = get_object_or_404(User, id=user_id)
        if target == request.user:
            return Response({'error': 'You cannot follow yourself'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(target)
        return Response({'status': 'followed', 'user': target.username})


class UnfollowUserView(generics.GenericAPIView):
    queryset = User.objects.all()

    def post(self, request, user_id):
        target = get_object_or_404(User, id=user_id)
        request.user.following.remove(target)
        return Response({'status': 'unfollowed', 'user': target.username})
