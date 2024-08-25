"""
URL configuration for Resturant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from Base_app.views import * 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",home, name='home'),
    path("about/",about, name='about'),
    path("order/",order, name='order'),
    path("book_table/",book_table, name='book_table'),
    path("contact/",contact, name='contact'),
    path("menu/",menu, name='menu'),
    path("feedback/",feedback, name='feedback'),
]
if settings.DEBUG: 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
