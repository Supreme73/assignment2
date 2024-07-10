from django.shortcuts import render
from .models import Category, Product
from django.http import JsonResponse
from .api_file.serializer import CategorySerializer, ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.
#class CategoryView(APIView):
 #   def get(self, request):
 #       categor = Category.objects.all()
  #      serializer = CategorySerializer(categor, many= True, context={'request': request})
 #       return Response(serializer.data)
    
  #  def post (self, request):
   #     serializer = CategorySerializer(data=request.data)
   #     if serializer.is_valid():
   #         serializer.save()
   #         return Response(serializer.data)
   #     else:
   #         return (serializer.errors)
class CategoryView(generics.ListAPIView):
    
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset

class ProductView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
    
    