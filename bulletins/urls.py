from django.urls import path

from bulletins.apps import BulletinsConfig
from bulletins.views import AdListApiView, AdRetrieveApiView, \
    AdCreateApiView, AdUpdateApiView, AdDestroyApiView, CommentListApiView, \
    CommentCreateApiView, CommentUpdateApiView, CommentDestroyApiView

app_name = BulletinsConfig.name

urlpatterns = [
    path('ads/', AdListApiView.as_view(), name='ads_list'),
    path('ad/<int:pk>/', AdRetrieveApiView.as_view(),
         name='ad_detail'),
    path('ad/create/', AdCreateApiView.as_view(),
         name='ad_create'),
    path('ad/<int:pk>/update/', AdUpdateApiView.as_view(),
         name='ad_update'),
    path('ad/<int:pk>/delete/', AdDestroyApiView.as_view(),
         name='ad_delete'),
    path('comments/', CommentListApiView.as_view(), name='comments_list'),
    path('comment/create/', CommentCreateApiView.as_view(),
         name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateApiView.as_view(),
         name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDestroyApiView.as_view(),
         name='comment_delete'),
]
