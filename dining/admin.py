import requests
from django.contrib import admin
from django.urls import path
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

# Register your models here.
from dining.models import Menu, Item, DailyMenu, Feedback


class FeedbackAdmin(admin.TabularInline):
    model = Feedback
    extra = 1
    exclude = ['added_by', ]


class ItemAdmin(admin.ModelAdmin):
    model = Item


class MenuAdminInline(admin.TabularInline):
    model = Menu


@admin.register(DailyMenu)
class DailyMenuAdmin(admin.ModelAdmin):
    model = DailyMenu
    inlines = [
        MenuAdminInline,
        FeedbackAdmin,
    ]
    change_list_template = "send_email.html"

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.added_by = request.user
            instance.save()
        formset.save_m2m()

    def get_urls(self):
        urls = super().get_urls()
        my_url = [
            path('email/', self.send_email),
        ]
        return my_url + urls

    def send_email(self, request):
        menu_url = "http://localhost:8000/menu"
        r = requests.get(menu_url)
        content = r.text.replace("\n", "")
        send_mail('Menu for the week',
                  content,
                  'userfrom@example.com',
                  ['userto@example.com'],
                  fail_silently=False,
                  )
        self.message_user(request, "Email Sent Successfully")
        return HttpResponseRedirect("../")


admin.site.register(Menu)
admin.site.register(Item)
admin.site.register(Feedback)
