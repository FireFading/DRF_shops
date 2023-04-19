from django.test import TestCase
from streets.models import Street
from streets.tests.settings import STREET_NAME
from towns.models import Town
from towns.tests.settings import TOWN_NAME


class StreetModelTestCase(TestCase):
    def setUp(self):
        self.town = Town.objects.create(name=TOWN_NAME)
        self.street = Street.objects.create(name=STREET_NAME, town=self.town)

    def test_street_creation(self):
        self.assertEqual(self.street.name, STREET_NAME)
        self.assertEqual(self.street.town, self.town)

    def test_street_str_method(self):
        self.assertEqual(str(self.street), STREET_NAME)

    def test_street_verbose_name_plural(self):
        self.assertEqual(str(Street._meta.verbose_name_plural), "Улицы")

    def test_street_town_related_name(self):
        self.assertIn(self.street, self.town.shops.all())
