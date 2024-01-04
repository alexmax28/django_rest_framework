from rest_framework import serializers
from musics.models import Product


class ProdctSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('id', 'name', 'description', 'price', 'created_at')
        # fields = ('name', 'price')
