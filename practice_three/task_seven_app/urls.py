from .views import get_all_customer_orders_and_list_products
from django.urls import path


urlpatterns = [

    path('get_all_customer_orders_and_list_products/<str:name_client>/',
         get_all_customer_orders_and_list_products,
         name='get_all_customer_orders_and_list_products'),

]
