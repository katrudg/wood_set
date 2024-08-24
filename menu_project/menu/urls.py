from django.urls import path

from menu.views import example_view

urlpatterns = [
    path('', example_view, ),
]
