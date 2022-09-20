from django.urls import path
from shop_app.views import ProductViewSet, CategoryViewSet, CommentView, CartView, CartProductView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('product/', ProductViewSet.as_view({'get': 'list', 'post': 'create', })),
    path('product/<int:pk>', ProductViewSet.as_view({'get': 'retrieve', 'delete': 'destroy' })),
    path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('product/<int:pk>/', ProductViewSet.as_view(
        {
            'get': 'retrieve',
            'delete': 'destroy',
            'put': 'update',
            'patch': 'update'
        }
    )),
    path('category/<int:pk>/', CategoryViewSet.as_view(
        {
            'get': 'retrieve',
            'delete': 'destroy',
            'put': 'update',
            'patch': 'update'
        }
    )),
    path('product/<int:pk>/comment/create', CommentView.as_view({'post': 'create'})),

    path('add_to_cart', CartView.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'})),
    path('add_to_cart_product', CartProductView.as_view({'get': 'list', 'post': 'create', })),

    path('add_to_cart_product/<int:pk>/', CartProductView.as_view({'get': 'retrieve', 'post': 'create', 'delete': 'destroy', 'put': 'update'})),
    path('add_to_cart/<int:pk>/', CartView.as_view({'get': 'retrieve', 'post': 'create', 'delete': 'destroy', 'put': 'update'})),

]
