from django.urls import path

from . import views

urlpatterns = [
    path('menu/', views.MenuItemsView.as_view(), name='menus'),
    path('menu/<int:pk>', views.DailyDetailView.as_view(), name='menu-detail'),
]
