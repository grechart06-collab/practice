from django import forms
from .models import Registration


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'phone', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if not name:
            raise forms.ValidationError('Введите имя.')
        return name

    def clean_email(self):
        return self.cleaned_data['email'].strip().lower()

    def clean_phone(self):
        return self.cleaned_data['phone'].strip()

    def clean_comment(self):
        return self.cleaned_data['comment'].strip()
