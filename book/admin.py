from django.contrib import admin
from .models import (
    Author,
    Book,
    BookImage,
    Author,
    BookLanguage,
    BookCondition,
    Publisher,
    Category,
)


class BookImageInline(admin.TabularInline):
    model = BookImage
    extra = 1


@admin.register(Author)
class AuThorAdmin(admin.ModelAdmin):
    list_display = ["last_name"]


# Register your models here.


@admin.register(BookCondition)
class BookConditionAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(BookLanguage)
class BookLanguageAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["name", "author", "language", "publisher", "condition", "price"]
    inlines = [BookImageInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
