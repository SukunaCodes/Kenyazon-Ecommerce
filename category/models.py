from djongo import models


# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    category_image = models.ImageField(upload_to='photos/categories', blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'
