from django.db import models


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
    ingredients = models.TextField(verbose_name="Ингредиенты")
    image = models.ImageField('изображение')
    meal_type = models.CharField('тип приема пищи', max_length=20, choices=MEAL_TYPES)
    allergens = models.CharField(max_length=10, choices=ALLERGENS, verbose_name='аллергены')

    class Meta:
        verbose_name = 'блюдо'
        verbose_name_plural = 'блюда'

    def __str__(self):
        return self.name


# class Ingredient(models.Model):
#     name = models.CharField(
#         'название',
#         max_length=50,
#     )
#     price = models.DecimalField(
#         'цена за кг/л/шт',
#         max_digits=6,
#         decimal_places=2,
#         blank=True,
#         null=True
#     )
#     units = models.CharField(
#         'единицы измерения',
#         max_length=20,
#         blank=True,
#         null=True,
#     )

#     class Meta:
#         verbose_name = 'ингредиент'
#         verbose_name_plural = 'ингредиенты'

#     def __str__(self):
#         return self.name


# class IngredientPosition(models.Model):
#     ingredient = models.ForeignKey(
#         Ingredient,
#         verbose_name='ингредиент',
#         related_name='positions',
#         on_delete=models.CASCADE,
#     )
#     quantity = models.FloatField(
#         'число',
#     )

#     dish = models.ForeignKey(
#         Dish,
#         verbose_name='блюдо',
#         related_name='positions',
#         on_delete=models.CASCADE,
#     )

#     class Meta:
#         verbose_name = 'позиция ингредиентов блюда'
#         verbose_name_plural = 'позиции ингредиентов блюда'

#     def __str__(self):
#         return self.ingredient.name


# class MealPosition(models.Model):
#     meal = models.ForeignKey(
#         Meal,
#         verbose_name='прием пищи',
#         related_name='meal_positions',
#         on_delete=models.CASCADE,
#     )

#     dish = models.ForeignKey(
#         Dish,
#         verbose_name='блюдо',
#         related_name='dish_positions',
#         on_delete=models.CASCADE,
#     )
#     quantity = models.PositiveSmallIntegerField(
#         'число блюд',
#         validators=[MinValueValidator(1)],
#         default=1,
#     )

#     class Meta:
#         verbose_name = 'позиция приема пищи'
#         verbose_name_plural = 'позиции приема пищи'

#     def __str__(self):
#         return self.dish.name