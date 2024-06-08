from django.db import models


class Order(models.Model):
    user = models.CharField(max_length=200, null=False, blank=False)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    is_delivered = models.BooleanField(default=False)
    delivered_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    paid_info = models.JSONField(default=dict, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product_id = models.CharField(max_length=200, null=True, blank=True)
    product_name = models.CharField(max_length=200, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        ordering = ['product_name']
        unique_together = (('product_id', 'order'),)

    def __str__(self):
        return str(self.product_name)
