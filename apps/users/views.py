from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import get_user_model
from django.core.validators import ValidationError

User = get_user_model()


def sign_up(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password != repassword:
            raise ValidationError("Пароли не совпадают")

        if User.objects.filter(username=username).exists():
            return ValidationError("Такой пользователь существует")

        user = User.objects.create_user(
            username=username,
            password=password,
        )
        login(request, user)
        return HttpResponse("Вы успешно зарегистрировались")

