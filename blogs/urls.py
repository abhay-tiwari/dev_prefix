from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="blogs"),
    path('add/', views.add_blogs, name='add_blogs'),
    path('<slug>', views.blog, name='blog')
]