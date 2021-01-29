from django.shortcuts import (render,
                              redirect,
                              get_object_or_404)

from product.models import Product
from product.forms import ProductModelForm

from django.urls import reverse
from django.contrib import messages

from product.readerxl import readxl


def all_products(request):
    context = {
        'products': Product.objects.filter(is_active=True),
    }
    return render(request, 'product/all-products.html', context)


def product_details(request, pid):
    action = request.POST.get('action')

    if request.POST and action == 'delete':
        Product.objects.filter(id=pid).delete()
        messages.add_message(request, messages.INFO, f'{pid} has been deleted')
        return redirect(reverse('all_products'))

    if request.POST and action == 'deactivate':
        Product.objects.filter(id=pid).update(is_active=False)
        messages.add_message(request, messages.INFO, f'{pid} has been deactivated')
        return redirect(reverse('product_details', args=(pid,)))

    if request.POST and action == 'activate':
        product = Product.objects.get(id=pid)
        if product.quantity > 0:
            Product.objects.filter(id=pid).update(is_active=True)
            messages.add_message(request, messages.INFO, f'{pid} has been activated')
            return redirect(reverse('product_details', args=(pid,)))
        else:
            messages.add_message(request, messages.INFO, 'Not enough quantity!')

    # del request.session['cart']

    if request.POST and action == 'add to cart':

        cart = request.session.get('cart', {})  # get cart from session
        print('Cart: ', cart)

        product = Product.objects.values().get(id=pid)  # return dict
        print('Product: ', product)

        product['added_quantity'] = int(request.POST['qty'])  # write new key, value in product dict
        print('Product with qty: ', product)

        cart[str(pid)] = product
        print('Updated cart: ', cart)

        request.session['cart'] = cart
        print('Session: ', request.session.items())

    context = {
        'product': get_object_or_404(Product, id=pid),
    }
    return render(request, 'product/product.html', context)


def create_product(request):
    form = ProductModelForm(request.POST or None)
    if request.POST and form.is_valid():
        product = form.save(commit=True)
        print(request.POST)
        return redirect(reverse('product_details', args=(product.id,)))
    context = {
        'form': form,
    }
    return render(request, 'product/create-product.html', context)


def add_xl_file(request):
    if request.POST:
        uploaded_file = request.FILES['ExcelFile']
        readxl(uploaded_file.file)
        # return redirect(reverse('/'))
    return render(request, 'product/upload-products.html')


def user_cart(request):
    action = request.POST.get('action')

    if request.POST and action == 'delete':
        cart = request.session.get('cart', {})
        del cart[request.POST.get('pid')]
        request.session['cart'] = cart

    if request.POST and action == '+':
        cart = request.session.get('cart', {})
        product = cart[request.POST.get('pid')]
        in_storage = product['quantity']
        wanted = product['added_quantity']
        if in_storage > wanted:
            wanted += 1
            product['added_quantity'] = wanted
            request.session['cart'] = cart
        else:
            pass


    if request.POST and action == '-':
        cart = request.session.get('cart', {})
        product = cart[request.POST.get('pid')]
        in_storage = product['quantity']
        wanted = product['added_quantity']
        if wanted == 0:
            del cart[request.POST.get('pid')]
            request.session['cart'] = cart
        else:
            wanted -= 1
            product['added_quantity'] = wanted
            request.session['cart'] = cart

    return render(request, 'product/user-cart.html')
