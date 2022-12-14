from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("profile/", views.profile, name='profile'),
    path("update_profile/", views.update_profile, name='update_profile'),
    path("register/", views.register, name='register'),
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name="users/logout.html"), name='logout'),
    path("users/", views.show_users, name='users'),
    path("update_user/<int:pk>/update", views.update_user, name='update_user'),
    path("delete_user/<int:pk>/delete", views.delete_user, name='delete_user'),

    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
         name='password_reset'),
    path("password_reset_done/",
         auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
         name='password_reset_done'),
    path("password_reset_confirm/<uidb64>/<token>/",
         auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),
         name='password_reset_confirm'),
    path("password_reset_complete",
         auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
         name='password_reset_complete'),

]
