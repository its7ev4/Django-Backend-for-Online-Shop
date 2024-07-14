from django.urls import path # type: ignore
from . import views  

app_name = 'shop'
# маршрут привязывающий функцибю вида 
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>', views.single_course, name='single_course')
]