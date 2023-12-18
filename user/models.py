from django.db import models
from django.contrib.auth.models import AbstractUser
from book.models import GenderModel
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class UserModel(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name=_("User"),
        on_delete=models.CASCADE,
    )
    phone = models.CharField(_("Phone"), max_length=20)

    class Meta:
        verbose_name = _("UserModel")
        verbose_name_plural = _("UserModels")

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse("usermodel_detail", kwargs={"pk": self.pk})
    