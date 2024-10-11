from django.db import models

from item.models import Item
from user.models import User


# Create your models here.

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    # buyer_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # seller_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # status = models.ForeignKey(TransactionStatus)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateField()
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)

