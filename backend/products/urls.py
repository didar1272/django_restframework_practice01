from django.urls import path
from .views import (
    product_detail_view, 
    product_list_create_view,
    product_update_view,
    product_destroy_view,
    product_mixin_view
)

urlpatterns = [
    path('<int:pk>/', product_detail_view, name='product-detail'),
    path('', product_list_create_view, name='product-list-create'),
    path('<int:pk>/update/', product_update_view),
    path('<int:pk>/delete/', product_destroy_view),   
]