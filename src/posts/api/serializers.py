from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

from ..models import Post

post_detail_url = HyperlinkedIdentityField(
    view_name='posts-api:detail',
    lookup_field='slug'
)


class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'publish',
        ]


class PostDetailSerializer(ModelSerializer):
    url = post_detail_url

    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'title',
            'content',
            'publish',
        ]


class PostListSerializer(ModelSerializer):
    url = post_detail_url
    # delete_url = HyperlinkedIdentityField(
    #     view_name='posts-api:delete',
    #     lookup_field='slug'
    # )

    class Meta:
        model = Post
        fields = [
            'url',
            'title',
            'content',
            'publish',
        ]
