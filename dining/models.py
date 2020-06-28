from django.db import models
import datetime
from django.conf import settings


class Item(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class DailyMenu(models.Model):

    for_date = models.DateField()

    def __str__(self):
        day = self.for_date.strftime("%A")
        return u'%s(%s)' % (day, self.for_date)

    class Meta:
        ordering = ['for_date']


class Menu(models.Model):

    date = models.ForeignKey(DailyMenu, null=True, on_delete=models.CASCADE)
    BreakFast, Lunch, Snack = 'BREAKFAST', 'LUNCH', 'SNACK'
    menu_type = models.CharField(max_length=10, blank=True, null=True,
                                 choices=(
                                     (BreakFast, 'BREAKFAST'),
                                     (Lunch, 'LUNCH'),
                                     (Snack, 'SNACK'),
                                 )
                                 )
    items = models.ManyToManyField(Item)

    def __str__(self):
        return u'%s %s' % (self.menu_type, self.date)


class Feedback(models.Model):
    date = models.ForeignKey(DailyMenu, null=False, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '%s - %s' % (self.comment, self.added_by)
