from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('blogs/', views.get_all_blogs, name='all_blogs'),
    path('add-blog/', views.add_blog, name='add_blog'),
    path('update-blog/<int:blog_id>/', views.update_blog, name='update_blog'),
    path('delete-blog/', views.delete_blog, name='delete_blog'),
    path('publish-blog/', views.publish_blog, name='publish_blog')
]
