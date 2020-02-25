from django.shortcuts import render
from django.views import View
from  django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import Employee

class Index(View):
    template = 'frontend/index.html'

    def get(self, request):
        #return render(request, self.template)
        employees = Employee.objects.all()
        return render(request, self.template, {'employees': employees})

class Login(View):
    template = 'frontend/login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template, {'form': form})


    def post(self, request):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render(request, self.template, {'form': form})