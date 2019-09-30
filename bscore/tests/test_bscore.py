from django.test import TestCase, Client
from django.urls import reverse

from bscore.service.math_service import MathService


class TestBSCore(TestCase):

    client: Client

    def setUp(self) -> None:
        self.client = Client()

    def test_difference_calculation(self):
        value: int = MathService.calculate_difference(1)
        self.assertEqual(value, 0)
        value = MathService.calculate_difference(10)
        self.assertEqual(value, 2640)

    def test_occurrence_update_single_time(self):
        res = self.client.get(reverse('difference'), data={"number": 1})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()['data']['occurrence'], 1)
        self.assertEqual(res.json()['data']['value'], 0)

    def test_occurrence_update_multiple_times(self):
        res = self.client.get(reverse('difference'), data={"number": 1})
        res = self.client.get(reverse('difference'), data={"number": 1})
        res = self.client.get(reverse('difference'), data={"number": 1})
        res = self.client.get(reverse('difference'), data={"number": 1})
        res = self.client.get(reverse('difference'), data={"number": 1})
        self.assertEqual(res.json()['data']['occurrence'], 5)
        self.assertEqual(res.json()['data']['value'], 0)
