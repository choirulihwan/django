var updateBtns = document.getElementsByClassName('update-card');

for (i=0;i<updateBtns.length;i++) {
    updateBtns[i].addEventListener('click',  function() {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('Product id: ', productId, 'Action: ', action);

        console.log('User', user);
        if (user == 'AnonymousUser') {
//            console.log('User is not authenticated');
            addCookieItem(productId, action)
        } else {
           updateUserOrder(productId, action);
        }

    });
}

function updateUserOrder(productId, action) {
    console.log('User authenticated. sending data...');

    var url = '/update_item/';
    fetch(url, {
        method:'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId':productId, 'action':action})
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log('Data:', data);
            location.reload();
        });
}

function addCookieItem(productId, action) {
    console.log('User not login')

    if (action == 'add') {
        if (cart[productId] == undefined) {
            cart[productId] = {'quantity':1}
        } else {
            cart[productId]['quantity'] += 1
        }
    }

    if (action == 'remove') {
        cart[productId]['quantity'] -= 1;
        if (cart[productId]['quantity'] <= 0) {
            console.log('item will be deleted')
            delete cart[productId]
        }
    }
    console.log('cart:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/';
    location.reload()
}