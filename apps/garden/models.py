from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название сайта')
    logo = models.ImageField(upload_to='media/', verbose_name='Логотип сайта')
    description = models.TextField(verbose_name='Описание')
    phone = models.CharField(max_length=9, verbose_name='Телефон +996')
    email = models.EmailField(verbose_name='Email')
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'