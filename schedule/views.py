from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'schedule/index.html')


def courses_list(request):
    return HttpResponse("Список курсов")


def course_detail(request, course_id):
    if course_id > 100:  # несуществующий курс
        return redirect('home', permanent=False)
    return HttpResponse(f"Курс {course_id}")
