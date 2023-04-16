from django.http import HttpResponse
from django.urls import include, path

from recipes.views import contato, home, sobre

urlpatterns = [
    path(route='',    view=home),
    path(route='contato/', view=contato),
    path(route='sobre/',   view=sobre),
]
