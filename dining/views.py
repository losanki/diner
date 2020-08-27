from django.views.generic import ListView, DetailView, View, WeekArchiveView
from .models import Menu, Order, Meal
import datetime
from django.shortcuts import HttpResponseRedirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.dates import WEEKDAYS


def get_current_week():
    time = datetime.datetime.today().isocalendar()
    year = time[0]
    week = time[1] - 1
    return year, week


class DashboardView(View):

    def get(self, request):
        year, week = get_current_week()
        context = {'year': year, 'week': week}
        return render(request, 'dashboard.html', context=context)


class MenuItemsView(ListView):
    context_object_name = 'week_list'
    model = Menu
    dow = datetime.date.weekday(datetime.date.today())  # get current day of week e.g, 6
    mon = datetime.datetime.now() - datetime.timedelta(days=dow)
    weekend = mon + datetime.timedelta(days=5)
    queryset = Menu.objects.filter(date__gte=mon)
    queryset = queryset.filter(date__lte=weekend)
    template_name = 'week.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        weekday_names = []
        meal_names = ['Breakfast', 'Lunch', 'Snack']
        for i in range(6):
            weekday_names.append(WEEKDAYS[i])
        context['weekday_names'] = weekday_names
        context['meal_names'] = meal_names
        return context


class MenuWeekView(WeekArchiveView):
    queryset = Menu.objects.all()
    date_field = 'date'
    week_format = '%W'
    allow_future = True
    ordering = 'date'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        weekday_names = []
        for i in range(6):
            weekday_names.append(WEEKDAYS[i])
        context['weekday_names'] = weekday_names
        return context


class MenuDetailView(DetailView):
    model = Menu
    template_name = 'menu_detail.html'


class MealDetailView(DetailView):
    model = Meal

    def get_context_data(self, **kwargs):
        year, week = get_current_week()
        context = super().get_context_data(**kwargs)
        context['year'] = year
        context['week'] = week
        return context


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

