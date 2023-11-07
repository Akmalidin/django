"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.garden.views import index
from apps.garden.views import about
from apps.garden.views import team
from apps.garden.views import booking
from apps.garden.views import gallery
from apps.garden.views import portfolio
from apps.garden.views import contact
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('team/', team, name="team"),
    path('booking/', booking, name="booking"),
    path('gallery/', gallery, name="gallery"),
    path('portfolio/', portfolio, name="portfolio"),
    path('contact/', contact, name="contact"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)