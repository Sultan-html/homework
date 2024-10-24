from django.urls import path
from apps.main.views import main,event,artist,event_detail,blog,blog_detail

urlpatterns = [
    path('', main, name='main'),
    path('artist/',artist, name='artist'),
    path('event/', event, name='event'),
    path('event-detail/<int:id>/', event_detail, name='event_detail'),
    path('blog/',blog, name='blog' ),
    path('blog-detail/<int:id>/', blog_detail, name='blog_detail'),
]
