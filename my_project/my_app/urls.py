from django.urls import path
from .views.main_view import index,create_blog 
from .views.auth_view import register_page, login_page, logout_user


urlpatterns = [
    path('index/',index, name='index'),
    path('login/',login_page, name='login'),
    path('register/',register_page, name='register'),
    path('logout/', logout_user, name='logout'),
    path('create/',create_blog, name='create')
]
