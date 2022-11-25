from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Салам, брат, это главная страница сайта, лееее')


def group_posts(request, slug):
    return HttpResponse(f'Лееее, это страница номер {slug}, Чувствуй себя как дома')