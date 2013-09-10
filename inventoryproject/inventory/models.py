from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Category Name', max_length=100)
    description = models.TextField(null=True, blank=True)
    parent = ManyToManyField('self', null=True, blank=True)

    def __unicode__(self):
        return name

class Item(models.Model):
    name = models.CharField('item name', max_length=100)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    category = ManyToManyField(Category)

    def __unicode__(self):
        return name
