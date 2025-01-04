from django.shortcuts import render
from .models import Product  # Import your Product model

# Create your views here.


def index(request):
    products = Product.objects.all()  # Get all products from the database
    context = {
        'message': 'Hello from Django World!',
        'products': products,
        'items': ['Apple', 'Banana', 'Orange', 'Grapes'],
        'author': {
            'name': 'John Doe',
            'age': 30,
            'city': 'New York'
        },
        'books': ['Old Man and the Sea', 'The Great Gatsby', 'To Kill a Mockingbird'],
        'company': {'name': 'Acme Corp', 'address': {'street': '123 Main St', 'city': 'Anytown'}}
    }
    return render(request, 'myapp/index.html', context)

def about(request):
    context = {'message': 'About page'}  # Context is created HERE
    return render(request, 'myapp/about.html', context)

def contact(request):
    context = {'message': 'Contact page'}  # Context is created HERE
    return render(request, 'myapp/contact.html', context)