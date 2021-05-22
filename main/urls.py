from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home_page"),
    path("product/<str:id>/",view_product, name="view_product" )
]