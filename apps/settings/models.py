from django.db import models

# Create your models here.
class InfoUser(models.Model):
    image = models.ImageField(
        upload_to="image_user/",
        verbose_name='Фото'                 # Чтобы изменить язык (Отображается на русском)
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Введите ФИО'
    )
    work = models.CharField(
        max_length=50,
        verbose_name='Введите профессию'
    )
    description = models.TextField(verbose_name='Введите биографию')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Информация пользователя',
        verbose_name_plural = 'Информации пользователей'

class About(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    age = models.CharField(max_length=100, verbose_name='Возраст')
    nationality = models.CharField(max_length=100, verbose_name='Национальность')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Почта')
    telegram = models.CharField(max_length=100, verbose_name='Телеграм')
    labguage = models.CharField(max_length=100, verbose_name='Язык')
    year = models.CharField(max_length=100, verbose_name='Годы опыта')
    projects = models.CharField(max_length=100, verbose_name='Проекты')
    clients = models.CharField(max_length=100, verbose_name='Счастливые Клиенты')
    awards = models.CharField(max_length=100, verbose_name='Награды')
    def __str__(self):
        return f'{self.first_name} - {self.last_name}'
    class Meta:
        verbose_name = 'Обо мне',
        verbose_name_plural = 'Обо мне'

class Awards(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название навыка"
    )
    percent = models.CharField(
        max_length = 100,
        verbose_name = "Процент навыка"
    )
    
    def __str__(self):
        return f'Навык - {self.title}'
    class Meta:
        verbose_name = 'Мой навык',
        verbose_name_plural = 'Мои навыки'

class Education(models.Model):
    year = models.CharField(
        max_length = 255,
        verbose_name = "Год обучения"
    )
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    place = models.CharField(
        max_length = 255,
        verbose_name = "Место"
    )
    desc = models.TextField(verbose_name = "Описание")
    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = 'Мой опыт & оброзование',
        verbose_name_plural = 'Мои обучения'

class Portfolio(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название работы"
    )
    image = models.ImageField(
        upload_to='portfolio/',
        verbose_name='Фото'
    )
    project = models.CharField(
        max_length=255,
        verbose_name="Название проекта"
    )
    languages = models.CharField(
        max_length=255,
        verbose_name='Использованные языки прог'
    )
    client = models.CharField(
        max_length=255,
        verbose_name="Имя клиента"
    )
    preview = models.CharField(
        max_length=255,
        verbose_name='Сайт'
    )
    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = 'Моё портфолио',
        verbose_name_plural = 'Мои работы'

class Contact(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name = 'Имя'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    message = models.TextField(verbose_name = 'Сообщение')
    def __str__(self):
        return f"{self.name} -- {self.email}"
    class Meta:
        verbose_name = 'Обратная связь',
        verbose_name_plural = 'Обратная связь'

class Blog(models.Model):
    image = models.ImageField(
        upload_to='blogs/'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    suptitle = models.CharField(
        max_length=255,
        verbose_name='Описание'
    )
    def __str__(self):
        return f'{self.title}'
    class Meta:
        verbose_name = 'Мой блог',
        verbose_name_plural = 'Мои посты'