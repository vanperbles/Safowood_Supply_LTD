from django.db import models
from django.conf import settings
from django.shortcuts import reverse
# Create your models here.




class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name



class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(null=True, db_index=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    sealing_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.FloatField(blank=True, null=True)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="profile-images", blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name ='item'
        verbose_name_plural = 'items'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("item:detail", kwargs={
            'slug': self.slug
        })