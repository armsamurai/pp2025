from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()  # Получаем все проекты из базы
    context = {
        'projects': projects,
        'name': 'Ваше_имя',
        'job': 'Ваша_профессия'
    }
    return render(request, 'portfolio/index.html', context)


def contacts(request):
    context = {
        'phone': 'номер_телефона',
        'telegram': 'аккаунт_в_тг'
    }
    return render(request, 'portfolio/contacts.html', context)