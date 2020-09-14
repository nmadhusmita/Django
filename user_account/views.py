from lib2to3.fixes.fix_input import context

import form as form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    return render(request, 'user_account/index.html')


def sign_up(request):
    context = {}
    form = UserCreationForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'user_account/index.html')

    context['form'] = form
    return render(request, 'registration/sign_up.html', context)