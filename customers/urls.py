# This is used to define URL patterns for the app
from django.urls import path

# Import all views from the current (customers)app,Views contain the logic that runs when a URL is accessed
from . import views

# urlpatterns is a list that connects URLs to their respective views
urlpatterns = [

    # When the user visits 'account/' in the browser,Django will call the show_account function from views.py
    # name='account' is used to refer to this URL inside templates and code
    path('account/', views.show_account, name='account'),

    # When the user visits 'logout/',Django will call the sign_out function from views.py
    # name='logout' helps in using {% url 'logout' %} in templates
    path('logout/', views.sign_out, name='logout'),
]
