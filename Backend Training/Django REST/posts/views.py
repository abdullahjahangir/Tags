from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets
from rest_framework.decorators import api_view, APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import PostSerializers
from .models import Post

"""Model ViewSet"""


class PostModelViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        return super().perform_create(serializer)


"""ViewSet"""


class PostViewSet(viewsets.ViewSet):
    serializer_class = PostSerializers
    queryset = Post.objects.all()

    def list(self, request: Request, format=None):
        posts = self.queryset
        serializer = self.serializer_class(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request: Request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request: Request, pk: int, format=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = self.serializer_class(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def update(self, request: Request, pk: int, format=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = self.serializer_class(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request: Request, pk: int, format=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = self.serializer_class(
            instance=post, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request: Request, pk: int, format=None):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=status.HTTP_200_OK)


"""Generic Class Based Views"""


class PostListCreateGenericView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
):
    serializer_class = PostSerializers
    queryset = Post.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostRetrieveUpdateDeleteGenericView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = PostSerializers
    queryset = Post.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


"""Class Based Views"""


class PostListCreateView(APIView):
    serializer_class = PostSerializers

    def get(self, request: Request, format=None):
        posts = Post.objects.all()
        serializer = self.serializer_class(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class POSTRetrieveUpdateDelete(APIView):
    serializer_class = PostSerializers

    def get(self, request: Request, pk: int, format=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = self.serializer_class(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int, format=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = self.serializer_class(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: Request, pk: int, format=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = self.serializer_class(
            instance=post, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int, format=None):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=status.HTTP_200_OK)


"""Function Based Views"""


@api_view(http_method_names=["GET", "POST"])
def post_lists(request: Request):
    if request.method == "GET":
        posts = Post.objects.all()
        serializer = PostSerializers(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = PostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["GET", "PUT", "PATCH", "DELETE"])
def post_detail(request: Request, pk: int = None):
    if request.method == "GET":
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializers(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializers(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "PATCH":
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializers(instance=post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        print("DELETE")
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=status.HTTP_200_OK)
