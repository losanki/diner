# import requests
from django.contrib import admin
# from django.urls import path
# from django.core.mail import send_mail
# from django.http import HttpResponseRedirect
#
# # Register your models here.

from dining.models import Menu, Meal, Item, Order


class ItemAdmin(admin.ModelAdmin):
    model = Item


class MealAdminInline(admin.TabularInline):
    model = Meal

    def get_extra(self, request, obj=None, **kwargs):
        if hasattr(obj, 'meals'):
            return 0
        else:
            return 3


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('date', )
    model = Order
    date_hierarchy = 'date'


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    model = Menu
    inlines = [
        MealAdminInline,
    ]


#     change_list_template = "send_email.html"
#
#     def get_urls(self):
#         urls = super().get_urls()
#         my_url = [
#             path('email/', self.send_email),
#         ]
#         return my_url + urls
#
#     def send_email(self, request):
#         menu_url = "http://localhost:8000/menu"
#         r = requests.get(menu_url)
#         content = r.text.replace("\n", "")
#         send_mail('Menu for the week',
#                   content,
#                   'userfrom@example.com',
#                   ['userto@example.com'],
#                   fail_silently=False,
#                   )
#         self.message_user(request, "Email Sent Successfully")
#         return HttpResponseRedirect("../")


admin.site.register(Meal)
admin.site.register(Item)
