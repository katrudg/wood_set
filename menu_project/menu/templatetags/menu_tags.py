from django import template
from menu.models import MenuItem

register = template.Library()

@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.filter(menu__name=menu_name).select_related('parent')
    active_url = context['request'].path
    menu_dict = {}

    for item in menu_items:
        if item.parent_id is None:
            menu_dict[item] = []
        elif item.parent in menu_dict:
            menu_dict[item.parent].append(item)

    context.update({
        'menu_dict': menu_dict,
        'active_url': active_url,
    })
    return context
