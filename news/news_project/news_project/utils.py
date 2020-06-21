import random
import string

from django.template.defaulttags import register
from django.utils.text import slugify


def generate_sidebar(request):
    if request.user.is_authenticated:
        group_user = request.user.groups.all().first()
        parent_menu = group_user.menu_set.filter(parent_id=None, is_active=True)
        return parent_menu


@register.inclusion_tag('base/menu_child.html')
def children_tag(parent, groups):
    children = parent.menu_set.filter(parent_id=parent.id, is_active=True, groups=groups)
    return {'children': children}


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug = slug,
            randstr = random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug