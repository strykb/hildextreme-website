from django import forms
from django.core.mail import send_mail
from django.template.loader import render_to_string
from phonenumber_field.formfields import PhoneNumberField

class ContactForm(forms.Form):
    name = forms.CharField(label="Imię / Nazwa firmy",
                min_length=2,
                max_length=50,
                widget=forms.TextInput(attrs={"class":"form-control"}))
    message = forms.CharField(label="Wiadomość",
                widget=forms.Textarea(attrs={"class":"form-control"}))
    email = forms.EmailField(label="Email",
                min_length=10,
                max_length=800,
                widget=forms.TextInput(attrs={"class":"form-control"}))
    phone_number = PhoneNumberField(label="Numer telefonu",
                widget=forms.TextInput(attrs={"class":"form-control"}))

    phone_error = 'Upewnij się, że wprowadzono poprawny numer telefonu.'
    phone_number.error_messages['invalid'] = phone_error

    def send_email(self):
        # gets data from form
        subject = self.cleaned_data.get("name")
        email = self.cleaned_data.get("email")
        phone = self.cleaned_data.get("phone_number")
        content = self.cleaned_data.get("message")

        template_name = "main/email.txt"
        
        # passes data to template
        message = render_to_string(template_name, context={
            "content": content,
            "email": email,
            "phone": phone
        }, request=None, using=None)

        # sends email
        send_mail(subject, message, email,
            ["pawel.hildebrand@op.pl"], fail_silently=True)