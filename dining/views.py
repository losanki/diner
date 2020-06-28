from django.views.generic import ListView, DetailView, CreateView
from .models import DailyMenu, Feedback
import datetime
from .forms import CommentForm
from django.http import HttpResponseRedirect
from administration.models import Profile


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


class FeedbackCreate(CreateView):
    model = Feedback
    form_class = CommentForm
    success_url = '/menu'

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        ruser = request.user
        if form.is_valid():
            menu_id = kwargs['pk']
            menu = DailyMenu.objects.get(id=menu_id)
            user = Profile.objects.get(user=ruser)
            feedback = form.save(commit=False)
            feedback.date = menu
            feedback.added_by = user.user
            feedback.save()
            return HttpResponseRedirect("/menu")
