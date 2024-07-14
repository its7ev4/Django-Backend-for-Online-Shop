
from django.urls import path, include # type: ignore
from api.models import CourseResourse, CategoryResource
from tastypie.api import Api

api = Api(api_name='v1')
api.register(CourseResourse())
api.register(CategoryResource())


urlpatterns = [
    path('', include(api.urls), name = 'index')
]
