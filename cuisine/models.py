from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

from autoslug import AutoSlugField
from multiselectfield import MultiSelectField


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


class Subscription(models.Model):
    PERIOD = (
        ('1', '1 месяц'),
        ('3', '3 месяца'),
        ('6', '6 месяцев'),
        ('12', '12 месяцев')
    )
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
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    is_paid = models.BooleanField('Статус оплаты', default=False)
    period = models.CharField('Период', choices=PERIOD, default='1', max_length=10)
    started_at = models.DateTimeField('дата начала', default=timezone.now)
    ends_at = models.DateTimeField('дата окончания')
    meal_types = MultiSelectField('тип приема пищи', choices=MEAL_TYPES, max_length=50)
    allergy_types = MultiSelectField('аллергены', choices=ALLERGENS, max_length=50)
