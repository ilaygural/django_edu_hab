from django.urls import path, re_path, register_converter
from . import views
from . import converters

# noinspection PyTypeChecker
register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('about/', views.about, name='about'),
    path('post/', views.post_detail),
    path('', views.index, name='home'),  # http://127.0.0.1:8000/women/ добавлено имя
    path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive),
    path('archive/<year4:year>/', views.archive, name='archive'),
    path('posts/<int:year>', views.posts_list),

]
