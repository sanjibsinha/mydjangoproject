from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'message': 'Hello from Django World!',
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