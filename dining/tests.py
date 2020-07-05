from django.test import TestCase
from .models import Menu, Meal, Item
import datetime
from django.urls import reverse


class SimpleTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)

    def setUp(self):
        menu = Menu(date=datetime.datetime.now())
        dosa = Item.objects.create(name='Dosa', price=40)
        idli = Item.objects.create(name='Idli', price=40)
        self.dosa = dosa
        self.idli = idli
        meal = Meal(meal_type='SNACK')
        meal.save()
        meal.items.add(idli)
        meal.items.add(dosa)
        meal.menu = menu
        menu.save()
        meal.save()
        self.meal = meal

    def test_create_meal(self):
        meal = Meal(meal_type='SNACK')
        meal.save()
        meal.items.add(self.idli)
        meal.items.add(self.dosa)
        self.assertEqual(meal.meal_type, 'SNACK')

    def test_menu(self):
        menu = Menu.objects.first()
        # import pdb; pdb.set_trace()
        expected_item_name = menu.meals.first().items.first().name
        now = datetime.date.today()
        self.assertEqual(expected_item_name, 'Dosa')
        self.assertEqual(menu.date, now)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('menus'))
        self.assertEqual(resp.status_code, 200)

    def test_view_template(self):
        resp = self.client.get(reverse('menus'))
        self.assertTemplateUsed(resp, 'week.html')
