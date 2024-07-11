from django.shortcuts import render
from .models import Category, Product
from django.http import JsonResponse
from .api_file.serializer import CategorySerializer, ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import ProductForm
from .models import *
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

class ProductUploadView(FormView):
    template_name = 'upload_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('home')  # Replace 'success_url' with your actual success URL name

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    



class CategoryListView(ListView):
    model = Category
    template_name = 'hello.html'
    context_object_name = 'categories'

class CategoryView(ListView):
    template_name = 'categories.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context



    