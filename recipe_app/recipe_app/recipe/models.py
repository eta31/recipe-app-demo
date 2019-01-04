# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"

    def __unicode__(self):
        return self.category_name

class Recipe(models.Model):
    recipe_name = models.CharField(db_index=True, max_length=100)
    ingredients = models.CharField(max_length=255)
    instructions = models.TextField()
    serving_size = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    notes = models.TextField()
    created_date = models.DateTimeField(db_index=True,auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipe"
        ordering = ('created_date',)

    def __unicode__(self):
        return self.recipe_name



