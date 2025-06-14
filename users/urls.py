from django.urls import path
from .views import home,RegisterView
from . import views



urlpatterns = [
    path('',views.home, name='home'),
    path('register/', RegisterView.as_view(), name='users-register')
    
    
]


