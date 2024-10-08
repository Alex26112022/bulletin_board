from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    """ Сериализатор для пользователя."""
    class Meta:
        model = get_user_model()
        fields = (
            'email', 'password', 'first_name', 'last_name', 'phone', 'role',
            'image')
