from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Book,Category


@receiver(pre_save, sender=Book)
def get_real_price(sender, instance, *args, **kwargs):
    if instance.is_discount():
        instance.real_price = ((100 - instance.discount) / 100) * instance.price
    else:
        instance.real_price = instance.price
