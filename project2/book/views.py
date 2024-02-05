import rest_framework.status
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import action


# @action(detail=True, methods=["get"])
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['get'])
    def custom_action(self, request, pk=None):
        instance = self.get_object()
        print(f"aaaa:{instance}")
        # 在这里执行与实例相关的自定义逻辑。
        # 例如，您可以使用实例的信息执行一些操作。

        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def query_name(self, request):
        search_query = request.query_params.get('qname', '')
        queryset = Book.objects.filter(author=search_query)
        serializer = self.get_serializer(queryset, many=True)
        # 在这里执行与实例相关的自定义逻辑。
        # 例如，您可以使用实例的信息执行一些操作。

        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def query_title(self, request):
        search_query = request.query_params.get('qtitle', '')
        queryset = Book.objects.filter(title=search_query)
        if queryset:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "not find"}, status=rest_framework.status.HTTP_400_BAD_REQUEST)

    # @action(detail=True, methods=['post'])
    # def custom_post_action_with_params(self, request, pk=None):
    #     """
    #     接受带有参数的 POST 请求的自定义动作。
    #     """
    #     instance = self.get_object()
    #
    #     # 获取请求中传递的参数
    #     data = request.data.get('data', None)
    #
    #     if data is not None:
    #         # 在这里执行基于参数的逻辑，例如，更新模型实例
    #         instance.some_field = data
    #         instance.save()
    #
    #         serializer = self.get_serializer(instance)
    #         return Response(serializer.data)
    #     else:
    #         return Response({'error': 'custom_param is required'}, status=status.HTTP_400_BAD_REQUEST)
