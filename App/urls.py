from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', views.login, name='login'),
    # path('detail/<slug:slug>/', views.detail_blog, name='detail'),S
]