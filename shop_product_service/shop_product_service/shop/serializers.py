from rest_framework import serializers
from shop.models import Category, Product, ProductImage

class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ('url','pk','name', 'image',  'products')

        extra_kwargs = {'products': {'read_only': True}}


class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.SlugRelatedField(
        queryset=Product.objects.all(),
        slug_field='name',
    )
    class Meta:
        model = ProductImage
        fields = ('url','pk','product','label', 'image', 'description')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='name',
    )
    product_images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('url','pk','name','price','category', 'image', 'description', 'is_available', 'product_images')
