"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from botov.views import index, getCarFee, getCurrentTime, getImageRecognition
from store.views import createCustomer, getOrderStatus, getPreviousOrder

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name="index"),
    url(r'^api/v1.0/vehiculos/',getCarFee, name="getFee"),
    url(r'^api/v1.0/bot/', getCurrentTime, name="getCurrentTime"),
    url(r'^api/v1.0/image/', getImageRecognition, name="getImageRecognition"),
    url(r'^api/v2.0/store/create_customer/',createCustomer, name="createCustomer"),
    url(r'^api/v2.0/store/get_order_status/',getOrderStatus, name="getOrderStatus"),
    url(r'^api/v2.0/store/get_previous_order/',getPreviousOrder, name="getPreviousOrder"),
]
