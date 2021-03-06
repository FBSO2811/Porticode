from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from books.models import Book, UserProfile


# Create your views here.

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('welcome')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'accounts/signup.html')


def profile(request):
    books = Book.objects.filter(original_poster=request.user).order_by('title')
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {"books": books, "user_profile": user_profile})
