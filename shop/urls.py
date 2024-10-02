from django.urls import path
from .views import *


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),



    path('', ProductListViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('<int:pk>/', ProductDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='product_list'),

    path('users/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('users/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                       'delete': 'destroy'}), name='user_list'),

    path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                        'delete': 'destroy'}), name='category_list'),

    path('rating/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='rating_list'),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='rating_list'),

    path('review/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review_list'),
    path('review/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='review_list'),

    path('photos/', ProductPhotosViewSet.as_view({'get': 'list', 'post': 'create'}), name='photos_list'),
    path('photos/<int:pk>/', ProductPhotosViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                          'delete': 'destroy'}), name='photos_list'),

    path('cart/', CartViewSet.as_view({'get': 'retrieve'}), name='cart_detail'),

    path('cart_items/', CartViewSet.as_view({'get': 'list', 'post': 'create', }), name='car_item_list'),
    path('cart_items/<int:pk>/', CartViewSet.as_view({'put': 'update', 'delete': 'destroy', })),
]
