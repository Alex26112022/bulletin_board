from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    """ Сериализатор для пользователя."""

    class Meta:
        model = get_user_model()
        fields = (
            'id', 'email', 'password', 'first_name', 'last_name', 'phone',
            'role', 'image')
        ref_name = 'my_user'

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
