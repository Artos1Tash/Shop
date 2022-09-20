from django.contrib.auth.models import User
from django.db.models import F, Count, Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from shop_app.models import Product, Category, ProductComment, ProductLike, Cart, Cart_product
from shop_app.permissions import ProductPermission
from shop_app.serializers import ProductSerializer, CategorySerializer, ProductCommentSerializer, ProductDetailSerializer, CartSerializer, CartProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    serializer_classes = {
        'retrieve': ProductDetailSerializer,
    }
    lookup_field = 'pk'
    permission_classes = (ProductPermission,)
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'price']
    search_fields = ['name', 'description']
    ordering_fields = ['id', 'price']


    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

    def get_queryset(self):
        queryset = Product.objects.annotate(
            category_name=F('category__name'),
            owner_name=F('user__username'),
            likes_count=Count('likes')
        ).order_by('-id')
        return queryset

    # def get_queryset(self):
    #     queryset = Product.objects.prefetch_related(
    #         'category',
    #         Prefetch('user', queryset=User.objects.only('username', 'id'))
    #     ).order_by('-id')
    #     return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoryViewSet(ModelViewSet):
    # queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.annotate(
            product_count=Count('product')
        )
        return queryset


class CommentView(ModelViewSet):
    queryset = ProductComment.objects.all()
    serializer_class = ProductCommentSerializer
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(
            user=self.request.user,
            product_id=kwargs.get('product_pk')
        )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


class ProductLikeViewSet(APIView):

    def get(request, product_pk):
        created = ProductLike.objects.filter(product_id=product_pk, user=request.user).exists()
        if created:
            ProductLike.objects.filter(
                product_id=product_pk,
                user=request.user
            ).delete()
            return Response({'success': 'unliked'})
        else:
            ProductLike.objects.create(product_id=product_pk, user=request.user)
            return Response({'success': 'liked'})



class CartView(ModelViewSet):
    permissions_classes = [permissions.IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartProductView(ModelViewSet):
    permissions_classes = [permissions.IsAuthenticated]
    queryset = Cart_product.objects.all()
    serializer_class = CartProductSerializer
