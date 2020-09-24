from django.shortcuts import render


def store(request):
    context = {
        "title":"Store page"
    }
    return render(request, 'store.html', context)


def cart(request):
    context = {
        "title": "Cart page"
    }
    return render(request, 'cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)




