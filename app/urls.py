"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from product.views import (all_products,
                           product_details,
                           create_product,
                           add_xl_file)

urlpatterns = [
    path('', all_products, name='all_products'),
    path('create/', create_product, name='create_product'),
    path('upload_products/', add_xl_file, name='add_xl_file'),
    path('<int:pid>/delete/', product_details, name='delete_product'),
    path('<int:pid>/', product_details, name='product_details'),

    path('admin/', admin.site.urls),
]
