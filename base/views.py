from django.shortcuts import render, HttpResponse , redirect
import requests
from .models import register_user

def home(request):
    return render(request, 'index.html')

def book(request):
    return render(request, 'book.html')

def getstationCodes(station_name):

    url = "https://rstations.p.rapidapi.com/"

    payload = { "search": station_name }
    headers = {
        "content-type": "application/json",
        "Content-Type": "application/json",
        "X-RapidAPI-Key": "c090fd7df9msh49cf35a3307d4a7p1f848cjsnc3bf448a5a97",
        "X-RapidAPI-Host": "rstations.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    arr = response.json()
    print(arr)
    for i in arr:
        if i[1] == station_name:
            return i[0]
    return "Dummy"

def search_trains(request):   
    if request.method == "POST":
        src = request.POST.get('from')
        dest = request.POST.get('to')
        date = request.POST.get('date')

    src = getstationCodes(src)
    dest = getstationCodes(dest)

    url = "https://irctc1.p.rapidapi.com/api/v3/trainBetweenStations"

    querystring = {"fromStationCode":src,"toStationCode":dest,"dateOfJourney":date}

    headers = {
        "X-RapidAPI-Key": "c090fd7df9msh49cf35a3307d4a7p1f848cjsnc3bf448a5a97",
        "X-RapidAPI-Host": "irctc1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring).json()
    t=[]
    for i in range(0,5):
        if i<len(response['data']):
            trains = {
                "train_no" : response['data'][i]['train_number'],
                'train_name' : response['data'][i]['train_name'],
                'train_src' : response['data'][i]['train_src'],
                'train_dstn' : response['data'][i]['train_dstn'],
                'start_time' : response['data'][i]['from_std'],
                'reach_time' : response['data'][i]['to_sta']
            }
            t.append(trains)
            


    print(response)

    
    return render(request,'display.html',{'trains':t})




def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullname')
        e_mail = request.POST.get('email')
        pass_word = request.POST.get('password')

        user = register_user(full_name=full_name,e_mail=e_mail,pass_word=pass_word)
        user.save()
    return render(request,'register.html')

def login(request):
    print("Hello")
    if request.method == 'POST':
        search_email = request.POST.get('email')
        search_password = request.POST.get('password')
        for user in register_user.objects.all():
            if user.e_mail == search_email and user.pass_word == search_password:
                print("Present in Database")
                return redirect('home')
    return render(request,'login.html')