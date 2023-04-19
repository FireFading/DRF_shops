from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from shops.models import Shop
from shops.serializers import ShopSerializer
from streets.models import Street
from towns.models import Town


class ShopsViewTest(APITestCase):
    def setUp(self):
        self.town1 = Town.objects.create(name="Town 1")
        self.town2 = Town.objects.create(name="Town 2")
        self.street1 = Street.objects.create(name="Street 1", town=self.town1)
        self.street2 = Street.objects.create(name="Street 2", town=self.town2)
        self.shop1 = Shop.objects.create(
            name="Shop 1",
            street=self.street1,
            opening_time="09:00:00",
            closing_time="17:00:00",
        )
        self.shop2 = Shop.objects.create(
            name="Shop 2",
            street=self.street2,
            opening_time="09:00:00",
            closing_time="18:00:00",
        )
        self.url = reverse("shops:list")
        self.shop_data = {
            "name": "Shop 3",
            "street": self.street1.id,
            "opening_time": "08:30:00",
            "closing_time": "16:30:00",
        }
        self.wrong_shop_data = {
            "name": "Shop 5",
            "street": 100000,
            "opening_time": "08:30:00",
            "closing_time": "16:30:00",
        }

    def test_list_shops(self):
        response = self.client.get(path=self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_post_valid_data(self):
        response = self.client.post(self.url, self.shop_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data,
            ShopSerializer(Shop.objects.filter(name="Shop 3").first()).data,
        )

    def test_post_invalid_street_id(self):
        response = self.client.post(self.url, self.wrong_shop_data)
        # self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"error": "This street does not exist."})

    def test_get_all_shops(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, ShopSerializer(Shop.objects.all(), many=True).data)

    def test_get_shops_by_town_id(self):
        url = f"{self.url}?town_id={self.town1.id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            ShopSerializer(Shop.objects.filter(street__town=self.town1), many=True).data,
        )

    def test_get_shops_by_street_id(self):
        url = f"{self.url}?street_id={self.street2.id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            ShopSerializer(Shop.objects.filter(street=self.street2), many=True).data,
        )
