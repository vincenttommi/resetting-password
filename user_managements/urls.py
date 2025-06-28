from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from users.views import CustomLoginView
from users.forms import LoginForm

     
#     # path('logout/',LogoutView.as_view(template_name='users/logout.html'), name='logout'),




urlpatterns = [
    path('admin/', admin.site.urls),

    # Namespace 'users'
    path('', include('users.urls')),

    # Standalone login URL
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True,template_name='users/login.html', authentication_form=LoginForm), name='login'),

    # Social auth
    path('oauth/', include('social_django.urls', namespace='social')),
]
