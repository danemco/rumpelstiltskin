from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Category Name', max_length=100)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

class Item(models.Model):
    name = models.CharField('item name', max_length=100)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    category = models.ManyToManyField(Category)

    def __unicode__(self):
        return self.name
