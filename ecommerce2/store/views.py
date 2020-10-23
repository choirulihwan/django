import datetime
import json

from django.http import JsonResponse
from django.shortcuts import render
from .models import *

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        order = {'get_total_order':0, 'get_count_order':0}

    products = Product.objects.all()
    context = {
        "title":"Store page",
        "products": products,
        "order": order
    }
    return render(request, 'store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_count_order
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:
            cart = {}
        items = []
        order = {'get_total_order':0, 'get_count_order':0, 'shipping':False}
        cartItems = order['get_count_order']

        for i in cart:
            cartItems += cart[i]['quantity']

            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            order['get_total_order'] = total
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

    context = {
        "items": items,
        "order": order,
        "cartItems": cartItems,
        "title": "Cart page"
    }

    return render(request, 'cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_total_order':0, 'get_count_order':0, 'shipping':'False'}

    context = {
        "items": items,
        "order": order,
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
    # print(request.body)
    data = json.loads(request.body)


    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.trans_id = transaction_id

        if total == order.get_total_order:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer = customer,
                order = order,
                address = data['shipping']['address'],
                city=data['shipping']['city'],
                zipcode = data['shipping']['zipcode'],
                state = data['shipping']['state']
            )

    else:
        print('User is not logged in')

    return JsonResponse('Payment complete!', safe=False)