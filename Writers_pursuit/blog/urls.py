from django.urls import path
from . import views
# from .views import ListView


urlpatterns = [
    # path('',views.PostListView.as_view(),name = "blog-home"),
    path('',views.home,name = "blog-home"),
    path('about/',views.about,name = "blog-about"),
    path('post/create/',views.post_create,name="blog-create"),
    path('post/<data>/',views.detailed_content, name = "blog-detail"),
]