from datetime import datetime
from enum import Enum

from django.db import models


# Create your models here.
class ProblemTypeEnum(Enum):
    DIFFERENCE = 'difference'
    PYTHAGOREAN_TRIPLET = 'pythagorean_triplet'


class Solution(models.Model):
    solution: str = models.CharField(max_length=256)
    problem: str = models.CharField(max_length=255, db_index=True)
    problem_type: str = models.CharField(max_length=255, db_index=True,
                                         choices=[(tag, tag.value) for tag in ProblemTypeEnum])
    occurrence: int = models.IntegerField(default=1)
    created: datetime = models.DateTimeField(auto_now_add=True)
    updated: datetime = models.DateTimeField(auto_now=True)
