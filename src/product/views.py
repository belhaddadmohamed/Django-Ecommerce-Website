from django.shortcuts import render, get_list_or_404
from .models import Product
from django.core.paginator import Paginator


def product_list(request):
    """
    Function takes a request as input 
    Paginator of 4 product in each page
    If the request has ?page=value --> take that value and return all the products of that page Else show products of page-1 
    """

    # Get all the Product objects from the Database
    product_list = Product.objects.all()

    # Paginator show 4 Products per page
    paginator = Paginator(product_list, 4)  
    page_number = request.GET.get("page")   # url/?page=page_number
    product_list_paginator = paginator.get_page(page_number) 
    
    # The list of products should be inside a Dictionary
    context = {'product_list': product_list_paginator}

    return render(request, 'Product/Ecommerce_Homepage.html', context)



def product_detail(request, slug):
    """
    Function takes a request and a primary key (id) and return a single product.
    """
    product = Product.objects.get(prdSlug=slug)
    context = {'product': product}

    return render(request, 'Product/Ecommerce_Product_page.html', context)


