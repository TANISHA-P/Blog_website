from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name="users/login.html"), name="users-login"), #this is an inbuilt class-based view
    path('register/', views.register, name = "users-register"),
    path('logout/',auth_views.LogoutView.as_view(template_name="users/logout.html"),name="users-logout"),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),name="reset_password"),
    path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),name="password_reset_confirm"),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),name="password_reset_complete"),
    path('profile/', views.profile,name="users-profile"),
    path('user_profile/<data>/',views.another_person_profile, name="another_user-profile"), #django dispatcher concept. i.e, passing info through the url.
    path('user_profile/<data>/<int:pageno>',views.another_person_profile, name="another_user-profilee"),
    path('search_user/',views.search_user, name="search_user"),
]
