from django.views.generic import ListView, DetailView, View
from .models import Menu, Order, Meal
import datetime
from django.shortcuts import HttpResponseRedirect, render
from django.contrib.auth.mixins import LoginRequiredMixin


class MenuItemsView(ListView):
    dow = datetime.date.isoweekday(datetime.datetime.now())
    context_object_name = 'week_list'
    model = Menu
    mon = datetime.datetime.now() - datetime.timedelta(days=dow)
    weekend = mon + datetime.timedelta(days=6)
    queryset = Menu.objects.filter(date__gte=mon)
    # queryset = Menu.objects.filter(date__lte=weekend)
    # queryset = queryset.filter(date__gte=mon)
    # import pdb; pdb.set_trace()
    template_name = 'week.html'


class MenuDetailView(DetailView):
    model = Menu
    template_name = 'menu_detail.html'


class MealDetailView(DetailView):
    model = Meal
    template_name = 'meal_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
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
        return HttpResponseRedirect("../")

