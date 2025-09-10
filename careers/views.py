from rest_framework import viewsets
from .models import Post
from .serializers import PostCreateListSerializer, PostUpdateSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_datetime')
    serializer_class = PostCreateListSerializer

    def get_serializer_class(self):
        if self.action in ['partial_update', 'update']:
            return PostUpdateSerializer
        return PostCreateListSerializer
