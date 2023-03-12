from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import path

from licores.views import *

urlpatterns = [
    
    path('Venta/add/',SaleCreateView.as_view(), name='venta_create'),
    #path('sale/list/', views.SaleListView.as_view(), name='venta_list'),
]