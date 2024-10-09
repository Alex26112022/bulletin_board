from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from djoser.views import UserViewSet
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    user = get_user_model()
    queryset = user.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class CustomUserViewSet(UserViewSet):
    def me(self, request, *args, **kwargs):
        pass

    def activation(self, request, *args, **kwargs):
        pass

    def resend_activation(self, request, *args, **kwargs):
        pass

    def reset_username(self, request, *args, **kwargs):
        pass

    def reset_username_confirm(self, request, *args, **kwargs):
        pass

    def set_username(self, request, *args, **kwargs):
        pass

    def set_password(self, request, *args, **kwargs):
        pass
