from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('hydropower/', views.hydropower, name='blog-hydropower'),
    path('solar_power/', views.solar_power, name='blog-solar_power'),
    path('wind_power/', views.wind_power, name='blog-wind_power'),
    path('sources/', views.sources, name='blog-sources')
]