from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Board
from .serializers import BoardSerializer


class PostList(APIView):

    def post(self, request):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        posts = Board.objects.all()
        serializer = BoardSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetail(APIView):

    def get_object(self, pk):
        try:
            return Board.objects.get(pk=pk)
        except Board.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = BoardSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = BoardSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def update_counter(self):
    #     self.Board_views = self.Board_views + 1
    #     self.save()


# class CommentDetail(APIView):
#     comments = Comment.objects.all()
#     serializer = CommentSerializer(comments, many=True)
#
#     def get(self, request, pk):
#         comments = self.get_object(pk)
#         serializer = CommentSerializer(comments)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         comments = self.get_object(pk)
#         serializer = CommentSerializer(comments, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         comments = self.get_object(pk)
#         comments.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
