from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.
def login(request):
    return render(request, 'registration/login.html')

#404 error handler
def error_404_view(request, exception):
    return render(request, '404.html', status=404)


def exit (request):
    logout(request)
    return redirect('/')


