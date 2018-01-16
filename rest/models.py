from django.db import models

# Create your models here.
class Item (models.Model):
    name = models.CharField(max_length = 40)
    price = models.FloatField()

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"


    def __unicode__(self):
        return self.name


class Order (models.Model):
    name = models.ForeignKey(Item , on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __unicode__(self):
        return self.id