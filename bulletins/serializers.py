from rest_framework.serializers import ModelSerializer

from bulletins.models import Ad, Comment


class AdSerializer(ModelSerializer):
    """ Сериализатор для объявлений. """

    class Meta:
        model = Ad
        fields = '__all__'


class AdCreateSerializer(ModelSerializer):
    """ Сериализатор для создания и редактирования объявлений. """

    class Meta:
        model = Ad
        fields = ('title', 'price', 'description')


class CommentSerializer(ModelSerializer):
    """ Сериализатор для комментариев. """

    class Meta:
        model = Comment
        fields = '__all__'


class CommentCreateSerializer(ModelSerializer):
    """ Сериализатор для создания комментариев. """

    class Meta:
        model = Comment
        fields = ('text', 'ad')


class CommentUpdateSerializer(ModelSerializer):
    """ Сериализатор для редактирования комментариев. """

    class Meta:
        model = Comment
        fields = ('text',)
