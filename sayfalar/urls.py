from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    )
from . import views

# app_name="sayfalar"

urlpatterns = [
    path('',views.home,name='home'),
    path('about/', views.about, name='about'),
    path('basvuru/', views.basvuru, name='basvuru'),
    path('contact/', views.contact, name='contact'),
    path('EmekliyeKredi.html', views.EmekliyeKredi, name='EmekliyeKredi'),
    path('ptt_kredi.html', views.ptt_kredi, name='ptt_kredi'),
    path('SicilBozuk.html', views.SicilBozuk, name='SicilBozuk'),
    path('Documents/KisiselVerilerinKorunmasi.pdf', views.kisisel, name='KisiselVerilerinKorunmasi.pdf'),
    path('posts/', PostListView.as_view(),name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),
    path('posts/new/', PostCreateView.as_view(),name='post-create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'),
]

