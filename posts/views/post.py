from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post
from posts.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(active=True).order_by('title')
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
