from rest_framework import serializers
from musics.models import Product, User


class ProdctSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('id', 'name', 'description', 'price', 'created_at')
        # fields = ('name', 'price')


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
