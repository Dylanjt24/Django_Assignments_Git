from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def index(req):
    context = {
        'products': Product.objects.all()
    }
    return render(req,'amadon/index.html', context)

def buy(req, product_id):
    added_price = float(Product.objects.get(id=product_id).price)
    req.session['price'] = added_price * float(req.POST['quantity'])
    req.session['total_products'] += int(req.POST['quantity'])
    req.session['total_spent'] += added_price * float(req.POST['quantity'])
    return redirect('amadon:checkout')

def checkout(req):
    if 'price' not in req.session:
        req.session['price'] = 0
    if 'total_products' not in req.session:
        req.session['total_products'] = 0
    if 'total_spent' not in req.session:
        req.session['total_spent'] = 0
    context = {
        'price': req.session['price'],
        'total_products': req.session['total_products'],
        'total_spent': req.session['total_spent']
    }
    return render(req, 'amadon/checkout.html', context)

def clear(req):
    req.session.clear()
    return redirect('amadon:checkout')