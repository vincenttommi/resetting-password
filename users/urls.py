from django.urls import path
from .views import RegisterView, home



urlpatterns  = [
   
    path('register/', RegisterView.as_view(), name='users-register'),
    path('', home, name='users-home')

]