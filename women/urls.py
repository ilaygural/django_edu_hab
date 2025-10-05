from django.urls import path, re_path, register_converter
from . import views
from . import converters

# noinspection PyTypeChecker
register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('post/', views.post_detail),
    path('', views.index),  # http://127.0.0.1:8000/women/
    path('cats/<int:cat_id>/', views.categories),
    path('cats/<slug:cat_slug>/', views.categories_by_slug),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive),
    path('archive/<year4:year>/', views.archive),
    path('posts/<int:year>', views.posts_list),

]
