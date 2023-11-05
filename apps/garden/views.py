from django.shortcuts import render
from .models import Settings
def index(request):
    settings = Settings.objects.latest('id')
    return render(request, 'index.html', locals())