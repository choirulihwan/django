import datetime
import json

from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from .utils import cookieCart, cartData, guestOrder

def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']

    products = Product.objects.all()
    context = {
        "title":"Store page",
        "products": products,
        "order": order,
        "cartItems": cartItems
    }
    return render(request, 'store.html', context)


def cart(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        "items": items,
        "order": order,
        "cartItems": cartItems,
        "title": "Cart page"
    }

    return render(request, 'cart.html', context)


def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        "items": items,
        "order": order,
        "cartItems": cartItems,
        "title": "Cart page"
    }

    return render(request, 'checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, create = Order.objects.get_or_create(customer=customer, complete=False)

    order_item, create = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        order_item.quantity = (order_item.quantity + 1)
    elif action == 'remove':
        order_item.quantity = (order_item.quantity - 1)

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    print(request.body)
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.trans_id = transaction_id
    if total == order.get_total_order:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            zipcode=data['shipping']['zipcode'],
            state=data['shipping']['state']
        )

    return JsonResponse('Payment complete!', safe=False)