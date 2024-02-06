import rest_framework.status
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import action

from django.db import connection


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
        if queryset:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "not find"}, status=rest_framework.status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"])
    def query_title(self, request):
        search_query = request.query_params.get('qtitle', '')
        queryset = Book.objects.filter(title=search_query)
        if queryset:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "not find"}, status=rest_framework.status.HTTP_400_BAD_REQUEST)

    # post
    @action(detail=False, methods=['post'])
    def custom_post_action(self, request):
        # 獲取 JSON 參數
        json_data = request.data.get('json_param', {})

        serializer = BookSerializer(data=json_data)

        if serializer.is_valid():
            # 存入DB
            serializer.save()
            return Response(json_data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "false"}, status=rest_framework.status.HTTP_403_FORBIDDEN)

    # SQL
    @action(detail=False, methods=['get'])
    def sql_get(self, request):
        data = []
        search_query = request.query_params.get('qname', '')
        search_query2 = request.query_params.get('qtitle', '')
        # 執行原始的 SQL 查詢
        with connection.cursor() as cursor:
            cursor.execute(f'SELECT * FROM book WHERE author = "{search_query}" or title = "{search_query2}";')
            rows = cursor.fetchall()
            print(rows)
            for item in rows:
                resdata = {"id": item[0], "title": item[1], "author": item[2]}
                data.append(resdata)
        print(data)

        # 在這裡處理查詢結果
        # 例如，將結果轉換為字典或其他格式，然後返回
        # data = {"result": {"id": rows[0][0], "title": rows[0][1], "author": rows[0][2]}}
        # data = {"result": rows}
        return Response(data, status=status.HTTP_200_OK)
