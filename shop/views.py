from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Perfume, Order

# Public Views

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        messages.success(request, "Thank you for contacting us!")
        return redirect('contact')
    return render(request, 'contact.html')

def product(request):
    perfumes = Perfume.objects.all()
    return render(request, 'products.html', {'perfumes': perfumes})



# Authentication Views

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Signup successful! Please login.")
            return redirect('login')
        else:
            messages.error(request, "Signup failed. Please correct the errors below.")
    else:
        form = UserCreationForm()

    return render(request, 'shop/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('account')
        else:
            messages.error(request, "Invalid credentials")
    form = UserCreationForm()
    return render(request, 'account.html', {'form': form, 'login': True})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def account(request):
    return render(request, 'account.html', {'user': request.user})


# Account Management

@login_required
def update_account(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
        messages.success(request, "Account updated successfully!")
        return redirect('account')
    return render(request, 'update_account.html', {'user': request.user})

@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect('index')
    return redirect('account')


# Cart CRUD Views


@login_required
def add_to_cart(request, perfume_id):
    perfume = get_object_or_404(Perfume, id=perfume_id)
    order, created = Order.objects.get_or_create(
        user=request.user,
        perfume=perfume,
        defaults={'quantity': 1}
    )
    if not created:
        order.quantity += 1
        order.save()
    messages.success(request, f"{perfume.name} added to cart.")
    return redirect('cart')

@login_required
def view_cart(request):
    orders = Order.objects.filter(user=request.user)
    total_price = sum(order.total_price() for order in orders)
    return render(request, 'shop/cart.html', {'orders': orders, 'total_price': total_price})

@login_required
def update_cart(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            order.quantity = quantity
            order.save()
            messages.success(request, "Cart updated.")
        else:
            order.delete()
            messages.success(request, "Item removed from cart.")
    return redirect('cart')

@login_required
def delete_from_cart(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == 'POST':
        order.delete()
        messages.success(request, "Item removed from cart.")
    return redirect('cart')

@login_required
def empty_cart(request):
    Order.objects.filter(user=request.user).delete()
    messages.success(request, "Your cart has been emptied.")
    return redirect('cart')

# Custom Error Handler

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
