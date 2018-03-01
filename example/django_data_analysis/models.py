from django.db import models

# Create your models here.


class Order(models.Model):
    TYPE_CHOICE = (
        ("food", "food"),
        ("drink", "drink"),
    )
    type = models.CharField(max_length=31, choices=TYPE_CHOICE)
    createtime = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=1)
    total_price = models.IntegerField(default=1)
    amount = models.IntegerField(default=1)
