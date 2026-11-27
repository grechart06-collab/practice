from django.shortcuts import get_object_or_404, render
from django.template import TemplateDoesNotExist
from django.core.mail import send_mail
from django.db import IntegrityError, transaction
from .forms import RegistrationForm
from .models import Мероприятие, Registration


def index(request):
    events = Мероприятие.objects.filter(is_published=True).order_by('date')[:3]
    return render(request, 'main/index.html', {'events': events})


def event_list(request):
    events = Мероприятие.objects.filter(is_published=True).order_by('date')
    return render(request, 'main/events.html', {'events': events})


def event_detail(request, event_id):
    event = get_object_or_404(Мероприятие, id=event_id, is_published=True)
    form = RegistrationForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        registration = form.save(commit=False)
        registration.event = event
        if Registration.objects.filter(event=event, email=registration.email).exists():
            form.add_error('email', 'Вы уже зарегистрированы на это мероприятие.')
        else:
            try:
                with transaction.atomic():
                    registration.save()
            except IntegrityError:
                form.add_error('email', 'Вы уже зарегистрированы на это мероприятие.')
            else:
                send_mail(
                    f'Заявка на мероприятие «{event.event_name}»',
                    f"Здравствуйте, {registration.name}! Ваша заявка на мероприятие «{event.event_name}», которое состоится {event.date:%d.%m.%Y в %H:%M}, принята.",
                    None,
                    [registration.email],
                )
                return render(request, 'main/event_detail.html', {'event': event, 'form': RegistrationForm(), 'success': True})

    return render(request, 'main/event_detail.html', {'event': event, 'form': form})


def page_not_found(request, exception):
    try:
        return render(request, '404.html', status=404)
    except TemplateDoesNotExist:
        return render(request, 'main/404.html', status=404)
