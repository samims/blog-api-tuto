from rest_framework.serializers import ModelSerializer
from ..models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'content_type',
            'object_id',
            'parent',
            'content'
        ]
