from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from user.models import User


class Checkout(models.Model):
    order_notes = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("შეკვეთის დეტალები")
    )
    order_date = models.DateField(
        auto_now_add=True,
        verbose_name=_("შეკვეთის თარიღი")
    )
    product_cart = models.ForeignKey(
        "order.Cart",
        on_delete=models.CASCADE,
        verbose_name=_("მომხმარებლის კალათა"),
    )

    def __str__(self):
        return f"Order {self.id}"


class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name=_("მომხმარებელი")
    )
    flat_rate = models.IntegerField(default=5, verbose_name=_("მიტანა"))

    def __str__(self):
        return f"{self.user}"


class CartItem(models.Model):
    product = models.ForeignKey(
        "store.Product",
        on_delete=models.CASCADE,
        verbose_name=_("პროდუქტი")
    )
    product_quantity = models.IntegerField(verbose_name=_("რაოდენობა"))
    cart = models.ForeignKey(
        "order.Cart",
        on_delete=models.CASCADE,
        verbose_name=_("კალათა")
    )

    def __str__(self):
        return f"{self.product}"