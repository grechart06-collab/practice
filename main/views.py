from django.shortcuts import render
from .models import Мероприятие


def index(request):
    events = Мероприятие.objects.filter(is_published=True).order_by('date')
    return render(request, 'main/index.html', {'events': events})
