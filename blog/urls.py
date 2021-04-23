from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/Update', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('about/', views.about, name='blog-about'),
    path('hydropower/', views.hydropower, name='blog-hydropower'),
    path('solar_power/', views.solar_power, name='blog-solar_power'),
    path('wind_power/', views.wind_power, name='blog-wind_power'),
    path('sources/', views.sources, name='blog-sources')
]