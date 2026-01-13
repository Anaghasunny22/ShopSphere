from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def list_products(request):
    """_summary_

    return product list page

    Docstring for list_products
    
    :param request: Description
    """
    return render(request,'products.html')

def detail_products(request):
    return render(request,'product_detail.html')


