from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
#from rest_framework.routers import DefaultRouter
from .views import *

#router = DefaultRouter()

urlpatterns = [
    path('', CategoryListView.as_view(), name = 'home'),
    path( 'category/<str:pk>', CategoryView.as_view(), name = 'category'),
    path( 'update', ProductUploadView.as_view(), name = 'upload_product'),
    #path('products/',views.ProductView.as_view(), name = 'prods'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
