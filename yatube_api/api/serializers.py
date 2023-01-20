from django.shortcuts import get_object_or_404
from posts.models import User, Comment, Post, Group, Follow
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    class Meta:
        model = Comment
        fields = ('__all__')
        read_only_fields = ('author', 'post',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('__all__')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username', read_only=True,
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Follow

    def validate_following(self, value):
        """Проверка подписи на корректного пользователя"""
        following = get_object_or_404(User, username=value.username)
        user = self.context['request'].user
        follower = Follow.objects.filter(
            user=user, following=following).exists()
        if user == value:
            raise serializers.ValidationError('Нельзя подписаться на себя')
        if follower:
            raise serializers.ValidationError(
                'Вы уже подписаны на пользователя'
            )
        return value
