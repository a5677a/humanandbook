
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

#from accountapp import views
from accountapp.views import AccDetailView, AccUpdateView, AccDeleteView, SignupView
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'accountapp'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup', SignupView.as_view(), name='signup'),
    path('detail/<int:pk>', AccDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccDeleteView.as_view(), name='delete'),


]