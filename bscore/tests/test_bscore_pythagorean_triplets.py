from django.http import JsonResponse
from django.test import TestCase, Client
from django.urls import reverse

from bscore.service.math_service import MathService


class TestBSCore(TestCase):
    client: Client

    def setUp(self) -> None:
        self.client = Client()

    def test_pythagorean_calculation(self):
        sol, value = MathService.pythagorean_triplet(3, 4, 5)
        self.assertEqual(value, True)
        self.assertEqual(sol, 60)
        sol, value = MathService.pythagorean_triplet(6, 8, 10)
        self.assertEqual(value, True)
        self.assertEqual(sol, 480)
        sol, value = MathService.pythagorean_triplet(5, 12, 13)
        self.assertEqual(value, True)
        self.assertEqual(sol, 780)

    def test_pythagorean_update_single_time(self):
        res = self.client.get(reverse('pythagorean_triplets'), data={"a": 3, "b": 4, "c": 5})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()['data']['occurrence'], 1)
        self.assertEqual(res.json()['data']['is_triplet'], True)
        self.assertEqual(res.json()['data']['solution'], 60)

    def test_occurrence_update_multiple_times(self):
        res = self.client.get(reverse('pythagorean_triplets'), data={"a": 3, "b": 4, "c": 5})
        res = self.client.get(reverse('pythagorean_triplets'), data={"a": 3, "b": 4, "c": 5})
        res = self.client.get(reverse('pythagorean_triplets'), data={"a": 3, "b": 4, "c": 5})
        res = self.client.get(reverse('pythagorean_triplets'), data={"a": 3, "b": 4, "c": 5})
        res = self.client.get(reverse('pythagorean_triplets'), data={"a": 3, "b": 4, "c": 5})
        self.assertEqual(res.json()['data']['occurrence'], 5)
        self.assertEqual(res.json()['data']['is_triplet'], True)
        self.assertEqual(res.json()['data']['solution'], 60)

    def test_difference_with_invalid_params(self):
        res: JsonResponse = self.client.get(reverse('pythagorean_triplets'), data={"a": 3, "b": 4, "c": 15})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()['data']['is_triplet'], False)
        self.assertEqual(res.json()['data']['solution'], 180)
        res: JsonResponse = self.client.get(reverse('pythagorean_triplets'), data={"a": -3, "b": 4, "c": 5})
        self.assertEqual(res.status_code, 400)
        res: JsonResponse = self.client.get(reverse('pythagorean_triplets'), data={"a": 3.2, "b": 4.2, "c": 5})
        self.assertEqual(res.status_code, 400)
        res: JsonResponse = self.client.get(reverse('pythagorean_triplets'), data={"a": "hello", "b": 4, "c": 15})
        self.assertEqual(res.status_code, 400)
