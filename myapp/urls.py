from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Map the URL '/' to the 'index' view
    path('about/', views.about, name='about'),  # Map the URL '/about/' to the 'about' view
    path('contact/', views.contact, name='contact'),  # Map the URL '/contact/' to the 'contact' view
]