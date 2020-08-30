from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="blogs"),
    path('add/', views.add_blogs, name='add_blogs'),
    path('<slug:slug>', views.blog, name='blog'),
    path('add_comment/', views.add_comment, name="add_comment"),
    path('like_blog/', views.like_blog, name="like_blog")
]