from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated ,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def postlist(request):
    if request.method == 'GET':
        post = Post.objects.filter(status=True)
        serializers = PostSerializer(post, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializers = PostSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
        

    

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postdetail(request, id):
    post = get_object_or_404(Post, pk=id, status=True)
    if request.method == 'GET':
        serializers = PostSerializer(post)
        return Response(serializers.data)
    
    elif request.method == 'PUT':
        serializers = PostSerializer(post, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)

    elif request.method == 'DELETE':
        post.delete()
        return Response({'detail':'Item removed successfully'}, status=status.HTTP_204_NO_CONTENT)