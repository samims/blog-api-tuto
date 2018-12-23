from rest_framework.serializers import (HyperlinkedIdentityField,
                                        ModelSerializer, SerializerMethodField)

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
    user = SerializerMethodField()
    image = SerializerMethodField()
    html = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'user',
            'title',
            'content',
            'html',
            'publish',
            'image',

        ]

    def get_user(self, obj):
        return obj.user.username

    def get_image(self, obj):
        try:
            image = obj.image.url

        except ValueError:
            image = None
        return image

    def get_html(self, obj):
        return obj.get_markdown()


class PostListSerializer(ModelSerializer):
    url = post_detail_url
    user = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'title',
            'content',
            'publish',
        ]

    def get_user(self, obj):
        return obj.user.username
