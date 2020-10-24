from .models import *
import json

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    items = []
    order = {'get_total_order': 0, 'get_count_order': 0, 'shipping': False}
    cartItems = order['get_count_order']

    try:
        for i in cart:
            cartItems += cart[i]['quantity']

            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            order['get_total_order'] += total
            order['get_count_order'] += cart[i]['quantity']

            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageUrl': product.imageUrl
                },
                'quantity': cart[i]['quantity'],
                'get_total_price': total,
            }
            items.append(item)

            if product.digital == False:
                order['shipping'] = True

    except:
        pass

    return { 'cartItems':cartItems, 'order':order, 'items':items }


def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_count_order
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return { 'cartItems':cartItems, 'order':order, 'items':items }


def guestOrder(request, data):
    name = data['form']['name']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(
        email=email
    )
    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False
    )

    for item in items:
        product = Product.objects.get(id=item['product']['id'])
        order_item = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity']
        )

    return customer,order