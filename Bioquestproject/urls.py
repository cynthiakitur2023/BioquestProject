"""
URL configuration for Bioquestproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage, name = 'index'),
    path('delete/<id>', views.deleteData, name='deleteData'),
    path('insert', views.insertData, name='insertData'),
    path('about/',views.aboutpage, name = 'about'),
    path('contact/',views.contactpage, name = 'contact'),
    path('products/',views.productpage, name = 'products'),
    path('add/', views.add, name='add'),
    path('display/', views.display, name='display'),
    path('add_products/', views.add_products, name='add_products'),
    path('category_products/<id>', views.category_products, name='category_products'),
    path('singleproduct/<id>', views.singleproduct, name='single_products'),
    path('contactlist/', views.contactlist, name='contactlist'),
    path('filterprodut', views.filterprodut, name='filterprodut')
]
