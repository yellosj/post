from django.db import models
from rest_framework import serializers


# Create your models here.

class Board(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=10, null=False)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    # delete_date = models.DateTimeField(auto_now=True)
    # Board_views = models.PositiveIntegerField(default=0)


# like = models.
# bookmark = models.

# class Comment(models.Model):
#     board_id = models.ForeignKey(Board, on_delete=models.CASCADE)
#     author = models.CharField(max_length=10, blank=False)
#     author = models.CharField(max_length=10, blank=False)
#     comment = models.CharField(max_length=100, blank=False)
