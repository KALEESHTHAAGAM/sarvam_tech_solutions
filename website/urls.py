from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('service_details/', views.service_details, name='service_details'),
    path('projects/', views.projects, name='projects'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
]
