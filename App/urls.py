from django.urls import path

from . import views

app_name = 'Jakbeut'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    # path('detail/<slug:slug>/', views.detail_blog, name='detail'),S
]