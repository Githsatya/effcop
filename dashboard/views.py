from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import SliderValue
import json
from .forms import LoginForm
from django.contrib import auth, messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required
@csrf_exempt
def dashboard(request):
    return render(request, 'dashboard.html')


def update_slider(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        value = data.get('value')
        SliderValue.objects.create(user=request.user, value=value)
        last_five_values = list(SliderValue.objects.filter(user=request.user).order_by('-date')[:5].values_list('value', flat=True))
        return JsonResponse({'lastFiveValues': last_five_values})


def get_last_five(request):
    last_five_values = list(SliderValue.objects.filter(user=request.user).order_by('-date')[:5].values_list('value', flat=True))
    return JsonResponse({'lastFiveValues': last_five_values})

 
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login details')
    return render(request, 'login.html', {'form': LoginForm})

def logout(request):
    auth.logout(request)
    messages.info(request, 'You have been logged out!!')
    return redirect('login')