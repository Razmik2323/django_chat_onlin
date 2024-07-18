from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, logout


def frontpage(request):
    return render(request, 'core/frontpage.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})

class UserLogoutView(LogoutView):
    def get(self, request):
        logout(request)
        return redirect('login')

