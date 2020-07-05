from django.views.generic import ListView, DetailView, CreateView
from .models import DailyMenu
import datetime


class MenuItemsView(ListView):
    todat = datetime.date.isoweekday(datetime.datetime.now())
    context_object_name = 'week_list'
    model = DailyMenu
    queryset = DailyMenu.objects.filter(for_date__gt=datetime.datetime.now() - datetime.timedelta(days=todat))
    template_name = 'home.html'


class DailyDetailView(DetailView):
    model = DailyMenu
    template_name = 'menu_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm
        context['pk'] = self.kwargs['pk']
        return context
