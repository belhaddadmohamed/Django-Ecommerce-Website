from django.urls import path
from . import views


urlpatterns = [

    path("", views.product_list),
    path('product/<int:id>/', views.product_detail, name="product_detail"),

]