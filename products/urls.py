from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# URL patterns for this app
urlpatterns = [
    # Home page URL
    # Example: http://127.0.0.1:8000/
    path('', views.index, name='home'),

    # Product listing page
    # Example: http://127.0.0.1:8000/product_list
    path('product_list', views.list_products, name='list_product'),

    # Product detail page (dynamic URL with product ID)
    # Example: http://127.0.0.1:8000/product_detail/5/
    path('product_detail/<int:id>/', views.detail_products, name='detail_product'),
]


