from django.shortcuts import render
from menu.models import Menu

def example_view(request):
    menus = Menu.objects.all() 
    return render(request, 'menu/index.html', {'menus': menus})
