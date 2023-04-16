from django.urls import include, path

from recipes.views import home

urlpatterns = [
    path(route='',    view=home),

]
