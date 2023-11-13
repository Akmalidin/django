from django.shortcuts import render, redirect
from .models import InfoUser, About, Awards, Education, Portfolio, Blog, Contact
# Create your views here.

def index(request):
    infouser = InfoUser.objects.latest("id")      # Чтобы передать последние данные из class
    return render(request,"index.html", locals()) # locals -- чтобы использовать infouser во всех файлов

def about(request):
    about = About.objects.latest("id")
    awards = Awards.objects.all()
    education = Education.objects.all()
    return render(request,"about.html", locals())
def contact(request):
    about = About.objects.latest("id")
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        Contact.objects.create(name = name, email = email, message = message)
        return redirect('index')
    return render(request, "contact.html", locals())
def portfolio(request):
    portfolio = Portfolio.objects.all()
    return render(request, "portfolio.html", locals())
def blog(request):
    blog = Blog.objects.all()
    return render(request, 'blog.html', locals())