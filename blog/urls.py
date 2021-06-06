from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    #<int:category_id> CAMPO DINAMICO DE LA URL
    path('category/<int:category_id>/', views.category, name='category'),
]