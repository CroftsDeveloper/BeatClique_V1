from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string

User = get_user_model()
token_generator = PasswordResetTokenGenerator()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True, request=None):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            # Generate token and UID for email verification link
            token = token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            link = reverse('accounts:verify_email', kwargs={'uidb64': uid, 'token': token})
            full_link = f'http://{request.get_host()}{link}'
            
            # Render the email template with the user and verification link
            email_context = {
                'user': user,
                'verification_url': full_link,
            }
            email_body = render_to_string('accounts/verification_email.html', email_context)
            
            # Send verification email using the rendered template
            send_mail(
                'Verify your email address',
                email_body,
                'beatclique.project@gmail.com',
                [user.email],
                fail_silently=False,
                html_message=email_body,
            )
        return user

# Removed AccountUpdateForm to disable email update functionality for now - will add back in for future developments
