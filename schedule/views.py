from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    data = {
        'title': '📅 Edu_Hub - Расписание',
        'description': 'Система управления учебным процессом',
        'features': ['Курсы', 'Уроки', 'Преподаватели', 'Студенты'],
        'stats': {
            'total_courses': 15,
            'active_teachers': 8,
            'students_count': 120
        }
    }
    return render(request, 'schedule/index.html', data)


def courses_list(request):
    return HttpResponse("Список курсов")


def course_detail(request, course_id):
    if course_id > 100:  # несуществующий курс
        return redirect('home', permanent=False)
    return HttpResponse(f"Курс {course_id}")
