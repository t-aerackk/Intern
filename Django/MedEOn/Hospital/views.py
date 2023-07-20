from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import requests

# Create your views here.
def patient_view(request):
    context = {
        'user': request.user,
    }
    return render(request, 'register.html', context)
def base(request):
    return render(request,'base.html') 
def opd(request):
    return render(request, 'opd.html')
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def search(request):
    return render(request, 'search.html')


# def posts_view(request):
#     posts = Post.objects.all()
#     return render(request, 'posts.html', {'posts': posts})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['Password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard') 
            # if user is not None:
            #     logout(request, user)
            # return redirect('home') # Replace 'home' with your desired redirect URL
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'register.html')

def Logout(request):
    logout(request,)
    return redirect('home')

def patient_list(request):
    patient_ac = Patient.objects.all()
    return render(request, 'dashboard.html', {'patient_ac': patient_ac})
def appoint(request):
    return render(request, 'appoint.html')
def news(request):
    return render(request, 'news.html')
from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    #Retrieve weather data from API
    api_key = '86f666aad217601c39b151be9336345e'
    city = 'New York' # Replace with user-selected city
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial'
    print(url)
    response = requests.get(url).json()
    print(response)
     #Parse response and store in context
    temperature = response['main']['temp']
    weather = response['weather']
    coordinate=response['coord']['lon']
    base = response['base']
    name = response['name']

    description = response['weather'][0]['main']
    context = {'temperature': temperature, 'description': description,'base':base,'name':name}
    return render(request, 'news.html', {'res':context})

def chuck_norris_joke(request):
    api_url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(api_url)

    if response.status_code == 200:
        joke_data = response.json()
        joke = joke_data['value']
    else:
        joke = "Failed to fetch Chuck Norris joke. Please try again later."

    return render(request, 'news.html', {'joke': joke})

def appoint(request):
    if request.method == 'POST':
        appointment_type=request.POST['appointment_type']
        preferred_location=request.POST['preferred_location']
        department=request.POST['department']
        signs_symptoms=request.POST['signs_symptoms']
        preferred_doctor=request.POST['preferred_doctor']
        date=request.POST['date']
        time=request.POST['time']

        ap1 = Appointment.objects.create(appointment_type=appointment_type,preferred_location=preferred_location,department=department,signs_symptoms=signs_symptoms,preferred_doctor=preferred_doctor,date=date,time=time)
        
        
    return render(request, 'appoint.html')

def display_appointments(request):
    apps = Appointment.objects.all()
    return render(request, 'dashboard.html', {'appointments': apps})