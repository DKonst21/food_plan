from django.db import models
# from django.template.defaultfilters import slugify
from django.urls import reverse

from autoslug import AutoSlugField


class Dish(models.Model):
    ALLERGENS = (
        ('FISH', 'рыба и морепродукты'),
        ('MEAT', 'мясо'),
        ('CEREAL', 'зерновые'),
        ('HONEY', 'продукты пчеловодства'),
        ('NUTS', 'орехи и бобовые'),
        ('MILK', 'молочные продукты'),
    )
    MEAL_TYPES = (
        ('BREAKFAST', 'завтрак'),
        ('LUNCH', 'обед'),
        ('DINNER', 'ужин'),
        ('DESSERT', 'десерт'),
    )
    name = models.CharField('название', max_length=50)
    recipe = models.TextField('рецепт', max_length=2000)
    ingredients = models.TextField(verbose_name='Ингредиенты')
    image = models.ImageField('изображение')
    meal_type = models.CharField('тип приема пищи', max_length=20, choices=MEAL_TYPES)
    allergens = models.CharField(max_length=10, choices=ALLERGENS, verbose_name='аллергены')
    slug = AutoSlugField(populate_from='name', unique=True)

    class Meta:
        verbose_name = 'блюдо'
        verbose_name_plural = 'блюда'

    def get_absolute_url(self):
        return reverse('card', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
