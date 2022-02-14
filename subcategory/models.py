from djongo import models
from category.models import Category

# Create your models here.


class Subcategory(models.Model):
    subcategory_name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    subcategory_image = models.ImageField(upload_to='photos/subcategories')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.subcategory_name

    class Meta:
        verbose_name_plural = 'Subcategories'
