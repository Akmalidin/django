from django.shortcuts import render
from .models import Settings
def index(request):
    settings = Settings.objects.latest('id')
    return render(request, 'index.html', locals())

def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')
def booking(request):
    return render(request, 'booking.html')
def gallery(request):
    return render(request, 'gallery.html')
def portfolio(request):
    return render(request, 'portfolio.html')
def contact(request):
    return render(request, 'contact.html')