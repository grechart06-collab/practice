
from django.db import models


class Мероприятие(models.Model):
    event_name = models.CharField('Название', max_length=200)
    short_description = models.CharField('Краткое описание', max_length=300, blank=True, default='')
    event_text = models.TextField('Описание мероприятия')
    date = models.DateTimeField('Дата проведения')
    location = models.CharField('Место проведения', max_length=200, blank=True, default='')
    image = models.ImageField('Изображение', upload_to='events/', blank=True, null=True)
    is_published = models.BooleanField('Опубликовано', default=False)
    capacity = models.PositiveIntegerField('Вместимость', blank=True, null=True)

    def __str__(self):
        return self.event_name


class Registration(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('confirmed', 'Подтверждена'),
        ('cancelled', 'Отменена'),
    ]

    event = models.ForeignKey(Мероприятие, on_delete=models.CASCADE, related_name='registrations')
    name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=20, blank=True)
    comment = models.TextField('Комментарий', blank=True)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField('Дата регистрации', auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['event', 'email'], name='unique_event_email')
        ]

    def __str__(self):
        return f'{self.name} — {self.event}'


class ContactMessage(models.Model):
    name = models.CharField('Имя', max_length=100)
    email = models.EmailField('Email')
    message = models.TextField('Сообщение')
    created_at = models.DateTimeField('Дата отправки', auto_now_add=True)

    def __str__(self):
        return f'{self.name} — {self.email}'
