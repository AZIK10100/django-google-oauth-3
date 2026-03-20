from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_page, name='logout_page'),
]


