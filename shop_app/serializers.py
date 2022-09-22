from shop_app.models import Category, Product, ProductLike, ProductComment, Cart, Cart_product \
    # , Cart, Cart_product
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:

        model = Product
        fields = ['name', 'price', 'user', 'category']
        extra_kwargs = {'user': {'read_only': True}}
        # fields = '__all__'


class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComment
        fields = '__all__'

class ProductDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(read_only=True)
    owner_name = serializers.CharField(read_only=True)
    comments = ProductCommentSerializer(many=True)
    likes_count = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ('id', 'category_name', 'description', 'image', 'owner_name', 'delivery', 'comments', 'likes_count')
        extra_kwargs = {'user': {'read_only': True}}


class CategorySerializer(serializers.ModelSerializer):
    class Meta:

        model = Category
        fields = '__all__'


class ProductLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLike
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_product
        fields = '__all__'

