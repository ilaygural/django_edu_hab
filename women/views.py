from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Страница приложения women")

def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id:{cat_id}</p>')

def categories_by_slug(request, cat_slug):
    if request.GET:  # данные по запросу GET URL
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id:{cat_slug}</p>')

def archive(request, year):
    if year > 2025:  # Проверка и вызов исключения
        raise Http404()
    return HttpResponse(f"<h1>Архив по годам</h1><p >{year}</p>")

# Функция для своего ответа на ошибку 404
def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

# функция-представление для задания 1
def post_detail(request):
    if request.GET:
        return HttpResponse("|".join([f'{k}={v}' for k, v in request.GET.items()]))
    return HttpResponse("GET is empty")


# функция-представление для задания 2
def posts_list(request, year):
    if not (1990 < year < 2023):
        raise Http404()
    return HttpResponse(f'posts: {year}')