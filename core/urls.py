# from django.contrib import admin
from django.urls import path
from api.views import get_all_items,get_add_fruits,get_fruits_type,get_fruits_name,get_fruits_price

urlpatterns = [
    path('grocery/',get_all_items),
    path('grocery/add/',get_add_fruits),
    path('grocery/type/<type>',get_fruits_type),
    path('grocery/name/<name>',get_fruits_name),
    path('grocery/price/<price>',get_fruits_name)

]
