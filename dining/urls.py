from django.urls import path
from django.conf.urls import url, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='dashboard.html'), name='dashboard'),
    path('menu/', views.MenuItemsView.as_view(), name='menus'),
    path('menu/<int:pk>/', views.MenuDetailView.as_view(), name='menu_detail'),
    path('meal/<int:pk>/', views.MealDetailView.as_view(), name='meal_detail'),
    path('meal/<int:pk>/order', views.OrderCreateView.as_view(), name='order'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
]
