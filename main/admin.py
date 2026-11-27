from django.contrib import admin
from .models import ContactMessage, Мероприятие, Registration

admin.site.register(Мероприятие)


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'event', 'status', 'created_at')
    list_filter = ('event', 'status')
    search_fields = ('name', 'email')
    ordering = ('-created_at',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    ordering = ('-created_at',)
