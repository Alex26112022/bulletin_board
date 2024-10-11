from rest_framework import filters
from rest_framework.generics import CreateAPIView, ListAPIView, \
    RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny
from bulletins.models import Ad, Comment
from bulletins.paginators import MyPaginator
from bulletins.permissions import IsAdmin, IsUser
from bulletins.serializers import AdSerializer, AdCreateSerializer, \
    CommentCreateSerializer, CommentSerializer, CommentUpdateSerializer


class AdCreateApiView(CreateAPIView):
    """ Создает новое объявление. """
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer

    def perform_create(self, serializer):
        bulletin = serializer.save(author=self.request.user)
        bulletin.save()


class AdListApiView(ListAPIView):
    """ Возвращает список всех объявлений. """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = MyPaginator
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    permission_classes = [AllowAny]


class AdRetrieveApiView(RetrieveAPIView):
    """ Возвращает информацию об объявлении. """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdUpdateApiView(UpdateAPIView):
    """ Редактирует объявление. """
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer
    permission_classes = [IsAdmin | IsUser]


class AdDestroyApiView(DestroyAPIView):
    """ Удаляет объявление. """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAdmin | IsUser]


class CommentCreateApiView(CreateAPIView):
    """ Создает новый отзыв. """
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)
        comment.save()


class CommentListApiView(ListAPIView):
    """ Возвращает список всех отзывов. """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentUpdateApiView(UpdateAPIView):
    """ Редактирует отзыв. """
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer
    permission_classes = [IsAdmin | IsUser]


class CommentDestroyApiView(DestroyAPIView):
    """ Удаляет отзыв. """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdmin | IsUser]
