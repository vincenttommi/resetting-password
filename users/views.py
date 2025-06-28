from django.views import View
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

class RegisterView(View):
    template_name = 'users/register.html'

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
    