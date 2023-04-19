from django.test import TestCase
from towns.models import Town
from towns.tests.settings import TOWN_NAME


class TownModelTestCase(TestCase):
    def setUp(self):
        self.town = Town.objects.create(name=TOWN_NAME)

    def test_town_creation(self):
        self.assertEqual(self.town.name, TOWN_NAME)

    def test_town_str_method(self):
        self.assertEqual(str(self.town), TOWN_NAME)

    def test_town_verbose_name_plural(self):
        self.assertEqual(str(Town._meta.verbose_name_plural), "Города")
