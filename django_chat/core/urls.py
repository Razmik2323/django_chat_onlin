from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views import UserLogoutView

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', UserLogoutView.as_view(http_method_names=['get', 'post', 'options']), name='logout'),
]