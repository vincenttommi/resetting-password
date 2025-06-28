from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from users.views import CustomLoginView
from users.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='users/login.html',authentication_form=LoginForm), name='login'),
    # path('logout/',LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('oauth/', include('social_django.urls', namespace='social')),
]
