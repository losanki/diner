from django.db import models
from django.shortcuts import reverse
from django.core.exceptions import ValidationError
from administration.models import Profile


class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name


class Menu(models.Model):

    date = models.DateField()

    def get_absolute_url(self):
        return reverse('menu_detail', args=[str(self.pk)])

    def __str__(self):
        day = self.date.strftime("%A")
        return u'%s(%s)' % (day, self.date)

    class Meta:
        ordering = ['date']


class Meal(models.Model):

    menu = models.ForeignKey(Menu, null=True, on_delete=models.CASCADE, related_name='meals')
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

    available = models.BooleanField(choices=BOOL_CHOICES, default=True)
    BreakFast, Lunch, Snack = 'BREAKFAST', 'LUNCH', 'SNACK'
    meal_type = models.CharField(max_length=10, blank=True, null=True,
                                 choices=(
                                     (BreakFast, 'BREAKFAST'),
                                     (Lunch, 'LUNCH'),
                                     (Snack, 'SNACK'),
                                 )
                                 )
    items = models.ManyToManyField(Item, blank=True)

    class Meta:
        ordering = ['meal_type']

    # def validate_unique(self, *args, **kwargs):
    #     super().validate_unique(*args, **kwargs)
    #
    #     if self.__class__.objects.filter(menu=self.menu, meal_type=self.meal_type).exists():
    #         raise ValidationError(message='This type of meal already exists', code='unique_together',)

    def get_absolute_url(self):
        return reverse('meal_detail', args=[str(self.pk)])
    
    def __str__(self):
        return u'%s %s' % (self.meal_type, self.menu)

