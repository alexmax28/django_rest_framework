from django.shortcuts import render
from flask import Response

# def hello_view(request):
#     context = {'data': "hello django", }
#     # permission_classes = (IsAuthenticated,)
#     return render(request, '../templates/hello_django.html', context
#                   )


from musics.models import Product, User
from musics.serializers import ProdctSerializers, UserSerializers

from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProdctSerializers
    permission_classes = (IsAuthenticated,)


class UserViewSet(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    serializer_class = UserSerializers

    # 權限
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        keyword = self.request.query_params.get('username', None)
        if keyword is not None:
            queryset = User.objects.filter(user_name=keyword)
            return queryset
        else:
            queryset = User.objects.all()
            return queryset
