from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView, ArchiveIndexView
from dining.models import Menu

from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('menu/', views.MenuItemsView.as_view(), name='menus'),
    path('<int:year>/week/<int:week>/', views.MenuWeekView.as_view(), name='menus-week'),
    path('menu-latest/', ArchiveIndexView.as_view(model=Menu, date_field='date'), name='menus-latest'),
    path('menu/<int:pk>/', views.MenuDetailView.as_view(), name='menu_detail'),
    path('meal/<int:pk>/', views.MealDetailView.as_view(), name='meal_detail'),
    path('meal/<int:pk>/order', views.OrderCreateView.as_view(), name='order'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
]
