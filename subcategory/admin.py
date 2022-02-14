from django.contrib import admin
from .models import Subcategory


# Register your models here.


class SubcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('subcategory_name',)}
    list_display = ('subcategory_name', 'slug')


admin.site.register(Subcategory, SubcategoryAdmin)
