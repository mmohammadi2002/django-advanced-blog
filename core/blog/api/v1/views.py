from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated ,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import PostSerializer, CategorySerializer
from blog.models import Post, Category
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination


"""@api_view(['GET', 'POST'])
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
        


"""
        

'''class PostList(APIView):
    """getting a list of posts and creating new posts"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request):
        """retriveing a list of posts"""
        post = Post.objects.filter(status=True)
        serializers = PostSerializer(post, many=True)
        return Response(serializers.data)


    def post(self, request):
        """creating a post with provided data"""
        serializers = PostSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)'''     



'''
class PostDetail(APIView):
    """getting detail of the post and edit plus removing it."""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request, id):
        """retrieving the post data"""
        post = get_object_or_404(Post, pk=id, status=True)
        serializers = self.serializer_class(post)
        return Response(serializers.data)

    def put(self, request, id):
        """editing the post data"""
        post = get_object_or_404(Post, pk=id, status=True)
        serializers = PostSerializer(post, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)

    def delete(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({'detail':'Item removed successfully'}, status=status.HTTP_204_NO_CONTENT)
        
'''

'''
class PostList(ListCreateAPIView):
    """getting a list of posts and creating new posts"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)



class PostDetail(RetrieveUpdateDestroyAPIView):
    """getting detail of the post and edit plus removing it."""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

'''


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {'category':['exact', 'in'], 'author':['exact'], 'status':['exact']}
    search_fields = ['title', 'content']    
    ordering_fields = ['published_date']
    pagination_class = DefaultPagination

class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()