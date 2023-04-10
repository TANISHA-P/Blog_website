from django.urls import path
from . import views
# from .views import ListView


urlpatterns = [
    # path('',views.PostListView.as_view(),name = "blog-home"),
    path('',views.home,name = "blog-home"),
    path('about/',views.about,name = "blog-about"),
    path('post/create/',views.post_create,name="blog-create"),
    path('post/<data>/',views.detailed_content, name = "blog-detail"), #here data has to be the title of the blog
    path('post/<data>/update',views.post_update, name = "blog-update"), #here data has to be the title of the blog
]