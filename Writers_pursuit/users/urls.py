from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name="users/login.html"), name="users-login"), #this is an inbuilt class-based view
    path('register/', views.register, name = "users-register"),
    path('logout/',auth_views.LogoutView.as_view(template_name="users/logout.html"),name="users-logout"),
    path('profile/', views.profile,name="users-profile"),
    path('user_profile/<data>/',views.another_person_profile, name="another_user-profile"), #django dispatcher concept. i.e, passing info through the url.
]
