from django.urls import path
from django.urls import re_path as url
from users import views
from .views import RegisterView, LoginView, UserView,LogoutView,UsersApi


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    url(r'^getusers$',views.UsersApi),
    url(r'^getusers/([0-9]+)$',views.UsersApi),
    
]
