from django.urls import path
from .views import ListArticles

urlpatterns = [
    path('products/', ListArticles.as_view(), name="products")
]
