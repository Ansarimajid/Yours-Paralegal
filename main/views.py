from django.shortcuts import render
from .models import *

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html' )

def quote(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        service = request.POST['service']
        massege = request.POST['massege']
        state = request.POST['state']
        city = request.POST['city']
        quote = Quote.objects.create(
        name = name,
        email = email,
        phone = phone,
        service = service,
        massege = massege,
        city = city,
        state = state,
        )
        quote.save()

    return render(request, 'get-a-quote.html')

def services(request):
    return render(request,'services.html' )

def about(request):
    return render(request,'about.html' )

def serviced(request):
    return render(request,'service-details.html' )
