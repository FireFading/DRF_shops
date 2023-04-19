from django.test import TestCase
from django.utils import timezone
from shops.models import Shop
from shops.tests.settings import SHOP_NAME
from streets.models import Street
from streets.tests.settings import STREET_NAME
from towns.models import Town
from towns.tests.settings import TOWN_NAME


class ShopModelTestCase(TestCase):
    def setUp(self):
        self.town = Town.objects.create(name=TOWN_NAME)
        self.street = Street.objects.create(name=STREET_NAME, town=self.town)
        self.shop = Shop.objects.create(
            name=SHOP_NAME, street=self.street, opening_time=timezone.now(), closing_time=timezone.now()
        )

    def test_shop_name_max_length(self):
        max_length = self.shop._meta.get_field("name").max_length
        self.assertEquals(max_length, 128)

    def test_shop_verbose_name(self):
        verbose_name = self.shop._meta.verbose_name
        self.assertEquals(verbose_name, "Магазин")

    def test_shop_verbose_name_plural(self):
        verbose_name_plural = self.shop._meta.verbose_name_plural
        self.assertEquals(verbose_name_plural, "Магазины")

    def test_shop_ordering(self):
        self.assertEqual(Shop._meta.ordering, ["-name"])

    def test_shop_string_representation(self):
        self.assertEqual(str(self.shop), SHOP_NAME)

    def test_shop_street_relationship(self):
        street = self.shop.street
        self.assertEqual(street, self.street)

    def test_shop_opening_time(self):
        opening_time = self.shop.opening_time
        self.assertTrue(isinstance(opening_time, type(timezone.datetime.now())))

    def test_shop_closing_time(self):
        closing_time = self.shop.closing_time
        self.assertTrue(isinstance(closing_time, type(timezone.datetime.now())))
