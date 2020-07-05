from django.urls import path

from . import views

urlpatterns = [
    path('menu/', views.MenuItemsView.as_view(), name='menus'),
    path('menu/<int:pk>', views.MenuDetailView.as_view(), name='menu-detail'),
    path('menu/<int:pk>/order', views.OrderCreateView.as_view(), name='order'),
]
