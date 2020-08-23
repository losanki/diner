from django.views.generic import ListView, DetailView, View
from .models import Menu, Order, Meal
import datetime
from django.shortcuts import HttpResponseRedirect, render
from django.contrib.auth.mixins import LoginRequiredMixin


class MenuItemsView(ListView):
    context_object_name = 'week_list'
    model = Menu
    dow = datetime.date.weekday(datetime.datetime.now()) # get current day of week e.g, 6
    mon = datetime.datetime.now() - datetime.timedelta(days=dow)
    weekend = mon + datetime.timedelta(days=5)
    queryset = Menu.objects.filter(date__gte=mon)
    queryset = queryset.filter(date__lte=weekend)
    template_name = 'week.html'


class MenuDetailView(DetailView):
    model = Menu
    template_name = 'menu_detail.html'


class MealDetailView(DetailView):
    model = Meal
    template_name = 'meal_detail.html'


class OrderCreateView(LoginRequiredMixin, View):
    model = Order
    template_name = 'order_form.html'

    def get(self, request, *args, **kwargs):
        meal = Meal.objects.get(pk=kwargs['pk'])
        context = {'meal': meal}
        return render(request, 'order_form.html', context)

    def post(self, request, *args, **kwargs):
        meal = Meal.objects.get(pk=kwargs['pk'])
        order = Order()
        order.meal = meal
        order.user = self.request.user.profile
        order.save()
        return HttpResponseRedirect("/menu")

