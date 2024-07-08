from django.core.cache import cache
from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from .tasks import send_welcome_email


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        # check cash
        cached_users = cache.get('users')
        if cached_users is not None:
            return cached_users

        # get users list from DB
        users = super().get_queryset()

        # save cash
        cache.set('users', users, timeout=60)

        return users


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        send_welcome_email.delay(user.id)


class UserUpdate(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
