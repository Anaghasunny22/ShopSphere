from django.shortcuts import render
from . models import Product
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    featured_products = Product.objects.order_by('-priority')[:4]
    latest_products = Product.objects.order_by('-id')[:4]
    context={
        'featured_products':featured_products,
        'latest_products':latest_products
    }
    return render(request,'index.html',context)

def list_products(request):
    product_list = Product.objects.order_by('priority')

    paginator = Paginator(product_list, 4)   # 2 products per page
    page_number = request.GET.get('page')    # page number from URL
    products = paginator.get_page(page_number)

    context = {
        'products': products
    }
    return render(request, 'products.html', context)

def detail_products(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})



