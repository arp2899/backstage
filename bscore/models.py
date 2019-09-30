from datetime import datetime
from enum import Enum

from django.db import models


class DifferenceSolution(models.Model):
    solution: int = models.IntegerField()
    number: int = models.IntegerField()

    occurrence: int = models.IntegerField(default=1)
    created: datetime = models.DateTimeField(auto_now_add=True)
    updated: datetime = models.DateTimeField(auto_now=True)


class PythagoreanTripletSolution(models.Model):
    number_a: int = models.IntegerField()
    number_b: int = models.IntegerField()
    number_c: int = models.IntegerField()
    solution: int = models.IntegerField()
    is_triplet: bool = models.BooleanField()

    occurrence: int = models.IntegerField(default=1)
    created: datetime = models.DateTimeField(auto_now_add=True)
    updated: datetime = models.DateTimeField(auto_now=True)
