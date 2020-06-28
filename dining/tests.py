from django.test import TestCase
from .models import DailyMenu, Menu, Item
import datetime
from django.urls import reverse


class SimpleTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)

    def setUp(self):
        DailyMenu.objects.create(for_date=datetime.datetime.now())
        Item.objects.create(name='Dosa')

    def test_menu_create(self):
        daily_menu = DailyMenu.objects.get(id=1)
        dm = DailyMenu.objects.get(id=1)
        item = Item.objects.get(id=1)
        m = Menu.objects.create(date=dm, menu_type='BREAKFAST')
        m.items.add(item)

        expected_item_name = f'{item.name}'
        now = datetime.date.today()
        self.assertEqual(expected_item_name, 'Dosa')
        self.assertEqual(daily_menu.for_date, now)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('menus'))
        self.assertEqual(resp.status_code, 200)

    def test_view_template(self):
        resp = self.client.get(reverse('menus'))
        self.assertTemplateUsed(resp, 'home.html')
