from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from .forms import CustomUserCreationForm, AccountUpdateForm
from payments.models import Order

User = get_user_model()
token_generator = PasswordResetTokenGenerator()

# View for registering new users
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Pass request to form's save method for email verification
            form.save(request=request)
            messages.success(request, 'Registration successful. Please check your email to verify your account.')
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# View for user login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if not user.email_verified:
                messages.error(request, 'Please verify your email address to login.')
                return redirect('accounts:login')
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')

# View for viewing user account details
@login_required
def account_view(request):
    if request.method == 'POST':
        user = request.user
        email = request.POST.get('email', user.email)
        user.email = email
        user.save()
        messages.success(request, 'Account details updated successfully.')  # Notify user of successful update
    return render(request, 'accounts/account.html')

# View for updating user account details
@login_required
def account_update(request):
    if request.method == 'POST':
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account details updated successfully.')
            return redirect('accounts:account')  # Redirect to the account page after updating
        else:
            messages.error(request, 'Error updating account details. Please correct the errors below.')
    else:
        form = AccountUpdateForm(instance=request.user)
    return render(request, 'accounts/account_update.html', {'form': form})

# View for logging out users
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.') # Notify user of successful logout
    return redirect('home')

# View for displaying order history
@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'accounts/order_history.html', {'orders': orders})

# Function for email verification
def verify_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        user.email_verified = True
        user.save()
        messages.success(request, 'Your email has been verified. You can now login.')
        return redirect('accounts:login')
    else:
        messages.error(request, 'The verification link is invalid or has expired.')
        return redirect('register')
