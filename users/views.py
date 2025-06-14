from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from users.forms import RegisterForm,LoginForm
from django.contrib.auth.views import LoginView



def home(request):
    return render(request, 'users/home.html')


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'
    
    def dispatch(self,request, *args, **kwargs):
        #will redirect to the homepage if a user tries to access the register page while logged in
      if request.user.is_authenticated:
          return redirect(to='/')
      
      #else  process dispatch as it otherwise normally would
      return super(RegisterView,self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect(to='login')  # or use: redirect('home') if you’ve named the URL

        return render(request, self.template_name, {'form': form})



class CustomLoginView(LoginView):
    form_class = LoginForm
    def form_invalid(self, form):
        remember_me = form.cleaned_data('remember_me')
        
        if not remember_me:
            #set session expiry to 0 seconds. so it will  automaticaly close the session after the browser is closed
            self.request.session.set_expiry(0)
            #Set session as modified to force data updates/cookie to be saved
            self.request.session.modified = True
            
            #else browser session will be  as long as session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)
    
   
   
   

