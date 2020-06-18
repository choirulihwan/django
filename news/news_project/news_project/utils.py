from django.template.defaulttags import register


def generate_sidebar(request):
    if request.user.is_authenticated:
        group_user = request.user.groups.all().first()
        parent_menu = group_user.menu_set.filter(parent_id=None)
        return parent_menu


@register.inclusion_tag('base/menu_child.html')
def children_tag(parent):
    children = parent.menu_set.filter(parent_id=parent.id)
    return {'children': children}