from django.shortcuts import render

# def hello_view(request):
#     context = {'data': "hello django", }
#     # permission_classes = (IsAuthenticated,)
#     return render(request, '../templates/hello_django.html', context
#                   )


from musics.models import Product
from musics.serializers import ProdctSerializers

from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProdctSerializers
    permission_classes = (IsAuthenticated,)
