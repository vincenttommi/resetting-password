from django.views import View
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, LoginForm

class RegisterView(View):
    
    template_name = 'users/register.html'

    def dispatch(self, request, *args, **kwargs):
        #will redirect to the home page if a user tries to access th request
        if request.user.is_authenticated:
            return redirect(to='/')
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, self.template_name, {'form': form})




#Classed based view  that extends  from the built in login view to add a remember me functionality
class  CustomLoginView(LoginView):
    
    form_class =  LoginForm
    
    def form_valid(self, form):
        
        remember_me  = form.cleaned_data.get('remember_me')
        
        if not  remember_me:
        #setting session expiry to 0 seconds.So it will automatically close the session after the broswer  is closed
        
        #Setting session as modified to force data  updates/cookie to be saved
         self.request.session.modified = True
         
         
        #else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_invalid(form)