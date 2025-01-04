from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)  # Can be empty
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): #for showing name instead of object in admin panel and other places
        return self.name