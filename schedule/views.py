from django.http import HttpResponse
from django.shortcuts import render, redirect


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


def courses_list(request):
    return HttpResponse("Список курсов")


def course_detail(request, course_id):
    if course_id > 100:  # несуществующий курс
        return redirect('home', permanent=False)
    return HttpResponse(f"Курс {course_id}")
