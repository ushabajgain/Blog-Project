from django.urls import path
from .views.main_view import index
from .views.auth_view import login_page
from .views.auth_view import register_page

urlpatterns = [
    path('index/',index, name='index'),
    path('login/',login_page, name='login'),
    path('register/',register_page, name='register')
]
