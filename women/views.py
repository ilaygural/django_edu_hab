from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.template.defaultfilters import slugify

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]

# Create your views here.
def index(request):
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'women/index.html', context=data)

def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})

def categories(request, cat_id):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id:{cat_id}</p>')


def categories_by_slug(request, cat_slug):
    if request.GET:  # данные по запросу GET URL
        print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>id:{cat_slug}</p>')


def archive(request, year):
    if year > 2025:  # Проверка и вызов исключения
        # return redirect("/")  # перенаправление на главную 302
        # return redirect('/', permanent=True)  # постоянное перенаправление 301
        # return redirect(index, permanent=True) # перенаправление с представлением
        # return HttpResponseRedirect('/')  # перенаправление 302 через класс
        # return redirect('home', permanent=True)  # перенаправление через имя
        # return redirect('cats', 'music')  # перенаправление с slug
        url_redirect = reverse('cats', args=('music',))  # вычисление маршрута
        return HttpResponseRedirect(url_redirect)
    return HttpResponse(f"<h1>Архив по годам</h1><p >{year}</p>")


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
