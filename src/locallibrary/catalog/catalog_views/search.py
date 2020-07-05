from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from ..models import Video
from ..pagination import CustomPagination
from ..serializers.video_serializer import VideoSerializer


class Search(generics.ListAPIView):
    serializer_class = VideoSerializer
    pagination_class = CustomPagination
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    search_fields = ('title', 'description')
    ordering_fields = ('published_at',)
    ordering = ('-published_at',)

    def get_queryset(self):
        return Video.objects.all()
