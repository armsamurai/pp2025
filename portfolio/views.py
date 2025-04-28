from django.shortcuts import render


def home(request):
    context = {
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