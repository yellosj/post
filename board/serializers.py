from rest_framework import serializers
from .models import Board


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'author', 'title', 'content', 'created_date']


# class CommentSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ['board_id', 'id', 'author', 'comment']