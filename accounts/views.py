from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, AccountUpdateForm
from payments.models import Order

# View for registering new users
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect after registration
            messages.success(request, 'Registration successful.')  # Notify user of successful registration
            return redirect('login')  # Direct users to login after registering
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
            login(request, user)
            messages.success(request, 'Login successful.')  # Notify user of successful login
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')  # Notify user of invalid credentials
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
            return redirect('account')  # Redirect to the account page after updating
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
