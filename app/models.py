from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from cloudinary.models import CloudinaryField

STATE_CHOICES = [
    ('andhra pradesh', 'andhra pradesh'),
]

CATEGORY_CHOICES = [
    ('Me', 'Medical'),
    ('Mec', 'Mechanical'),
    ('Eng', 'Engineering'),
]

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    rollNumber = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)
    phoneNumber = models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    product_img = CloudinaryField('image')
    product_imag = CloudinaryField('image')
    product_image = CloudinaryField('image')
    product_images = CloudinaryField('image')

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
