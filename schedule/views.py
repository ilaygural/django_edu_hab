from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("""<h1>📅 Расписание занятий</h1>
        <p>Это моё приложение для управления расписанием!</p>
        <ul>
            <li>Курсы</li>
            <li>Уроки</li>
            <li>Преподаватели</li>
            <li>Студенты</li>
        </ul>
        <a href="/admin/">Перейти в админку</a>
    """)