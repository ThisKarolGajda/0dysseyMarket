from django.db import models

from category.models import Category
from user.models import User


# Create your models here.

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    # images = models.ManyToManyField() # Image
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
