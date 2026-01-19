from django.shortcuts import render, get_object_or_404
from .models import Product
from django.core.paginator import Paginator

# ----------------------------
# Home Page View
# ----------------------------
def index(request):
    # Get top 4 featured products based on priority (higher priority first)
    featured_products = Product.objects.order_by('-priority')[:4]

    # Get latest 4 products based on ID (newest first)
    latest_products = Product.objects.order_by('-id')[:4]

    # Data sent to template
    context = {
        'featured_products': featured_products,
        'latest_products': latest_products
    }

    # Render home page template with data
    return render(request, 'index.html', context)


# ----------------------------
# Product List Page View
# ----------------------------
def list_products(request):
    # Get all products ordered by priority (low to high)
    product_list = Product.objects.order_by('priority')

    # Create paginator object (4 products per page)
    paginator = Paginator(product_list, 4)

    # Get current page number from URL (example: ?page=2)
    page_number = request.GET.get('page')

    # Get products for the current page
    products = paginator.get_page(page_number)

    # Data sent to template
    context = {
        'products': products
    }

    # Render products list page
    return render(request, 'products.html', context)


# ----------------------------
# Product Detail Page View
# ----------------------------
def detail_products(request, id):
    # Get single product by ID
    # If product does not exist, show 404 error page
    product = get_object_or_404(Product, id=id)

    # Render product detail page with selected product
    return render(request, 'product_detail.html', {'product': product})
