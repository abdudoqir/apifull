from django.db import models
from django.urls import reverse

from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


class CommonInfo(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(f"{self._meta.model_name}_detail", kwargs={"pk": self.pk})


class GenderModel(models.TextChoices):
    male = "male", "Male"
    female = "female", "Female"
    other = "other", "Other"

    def __str__(self):
        return self.value

    def get_absolute_url(self):
        return reverse("gendermodel_detail", kwargs={"pk": self.pk})


class Author(CommonInfo):
    last_name = models.CharField(_("Last Name"), max_length=50)
    gender = models.CharField(max_length=6, choices=GenderModel.choices)

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")


class BookLanguage(CommonInfo):
    class Meta:
        verbose_name = _("Book Language")
        verbose_name_plural = _("Book Languages")


class Publisher(CommonInfo):
    class Meta:
        verbose_name = _("Publisher")
        verbose_name_plural = _("Publishers")


class BookCondition(CommonInfo):
    class Meta:
        verbose_name = _("Book Condition")
        verbose_name_plural = _("Book Conditions")


class Book(CommonInfo):
    author = models.ForeignKey(
        Author,
        verbose_name=_("Author"),
        on_delete=models.CASCADE,
        related_name="books",
    )
    language = models.ForeignKey(
        BookLanguage,
        verbose_name=_("Language"),
        on_delete=models.CASCADE,
        related_name="books",
    )
    publisher = models.ForeignKey(
        Publisher,
        verbose_name=_("Publisher"),
        on_delete=models.CASCADE,
        related_name="books",
    )
    condition = models.ForeignKey(
        BookCondition,
        verbose_name=_("Condition"),
        on_delete=models.CASCADE,
        related_name="books",
    )
    book_isbn = models.CharField(_("ISBN"), max_length=13)
    wroted_type = models.CharField(_("Wroted Type"), max_length=50)
    page_count = models.IntegerField(_("Page Count"))
    size = models.CharField(_("Size"), max_length=50)
    book_created_at = models.DateTimeField(_("Book Created At"))
    starts = models.IntegerField(_("Starts"))
    description = models.TextField(_("Description"))
    category = models.ForeignKey(
        "Category",
        verbose_name=_("Category"),
        on_delete=models.CASCADE,
        related_name="books",
    )
    cash_status = models.BooleanField(_("Cash Status"), default=True)
    readed_count = models.IntegerField(_("Readed Count"), default=0)
    reding_count = models.IntegerField(_("Red   ing Count"), default=0)
    want_read_count = models.IntegerField(_("Want Read Count"), default=0)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2, default=0)
    real_price = models.DecimalField(_("Real Price"), max_digits=10, decimal_places=2, default=0)
    discount = models.IntegerField(
        _("Discount"),
        validators=[MinValueValidator(0), MaxValueValidator(99)],
        default=0,
    )

    def is_discount(self):
        return self.discount > 0

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")


class Category(CommonInfo):

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class BookImage(models.Model):
    book = models.ForeignKey(
        Book,
        verbose_name=_("Book"),
        on_delete=models.CASCADE,
        related_name="book_images",
    )
    image = models.ImageField(_("Image"), upload_to="book_images/")
    is_main = models.BooleanField(_("Is Main"), default=False)

    class Meta:
        verbose_name = _("Book Image")
        verbose_name_plural = _("Book Images")
