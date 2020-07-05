from rest_framework import serializers

from ..models import Video


class VideoSerializer(serializers.ModelSerializer):
    """Serializes a response object."""

    thumbnails = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = ('title', 'description', 'source', 'video_id', 'published_at', 'created_at', 'thumbnails')

    @staticmethod
    def get_thumbnails(obj):
        return obj.thumbnails
