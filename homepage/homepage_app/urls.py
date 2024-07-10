from django.urls import path
#from rest_framework.routers import DefaultRouter
from .import views

#router = DefaultRouter()

urlpatterns = [
    path( 'category/', views.CategoryView.as_view(), name = 'cat'),
    #path('products/',views.ProductView.as_view(), name = 'prods'),

]