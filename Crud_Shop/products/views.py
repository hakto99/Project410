# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from shopping_cart.models import Order
from .models import Product


#This function is used to get all the products that have been purchased by a user.
#first it gets all the product objects then filters them by the products that exists within the user profile
#This is to get all the products that are availble to the user and filter the ones the user already owns
def product_list(request):
    object_list = Product.objects.all()
    filtered_orders = Order.objects.filter(owner=request.user.profile, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
    	user_order = filtered_orders[0]
    	user_order_items = user_order.items.all()
    	current_order_products = [product.product for product in user_order_items]

    context = {
        'object_list': object_list,
        'current_order_products': current_order_products
    }

    return render(request, "products/product_list.html", context)