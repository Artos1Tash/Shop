from django.urls import path
from shop_app.views import ProductViewSet, CategoryViewSet, CommentView
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
    path('product/<int:pk>/comment/create', CommentView.as_view({'post': 'create'}))
]
