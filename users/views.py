from django.views import View
from .forms import RegisterForm
from django.shortcuts import render, redirect

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
