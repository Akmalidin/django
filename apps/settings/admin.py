from django.contrib import admin
from .models import InfoUser, About, Awards, Education, Portfolio, Blog, Contact            # Импортируем наш модель
# Register your models here.
admin.site.register(InfoUser)            # Регистрация модели
admin.site.register(About)
admin.site.register(Awards)
admin.site.register(Education)
admin.site.register(Portfolio)
admin.site.register(Blog)
admin.site.register(Contact)