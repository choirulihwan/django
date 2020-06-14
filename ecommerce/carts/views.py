from django.shortcuts import render

# Create your views here.
from carts.models import Cart


def cart_home(request):
    # print(dir(request.session))
    # request.session.set_expiry(300)
    # key = request.session.session_key
    # print(key)
    del request.session['cart_id']
    cart_id = request.session.get('cart_id', None)

    if cart_id is None:
        # print('create new cart')
        cart_obj = Cart.objects.create(user=None)
        request.session['cart_id'] = cart_obj.id
    else:
        print('Cart id exists')
        print(cart_id)
        cart_obj = Cart.objects.get(id=cart_id)
    return render(request, "carts/home.html", {})
