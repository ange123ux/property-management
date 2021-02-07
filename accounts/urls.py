from django.urls import path
from . import views
from . views import SignUpView 

urlpatterns = [
    path('login', views.login, name='login'),
    # path('register', views.register, name='register'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]
