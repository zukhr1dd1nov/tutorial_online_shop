from django.urls import path
from .views import PostListView, PostDetailView, CommentCreateView

app_name = 'blogs'

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('post/<int:pk>/comment',CommentCreateView.as_view(), name='comment')
]