from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update_slider/', views.update_slider, name='update_slider'),
    path('get_last_five/', views.get_last_five, name='get_last_five'),
]
