import json
from typing import List, Optional, Tuple

from django.db.models import QuerySet, F
from django.http import JsonResponse
from django.shortcuts import render

from bscore.models import DifferenceSolution, PythagoreanTripletSolution
from bscore.service.math_service import MathService
from bscore.service.res_service import ResService


def difference(request) -> JsonResponse:
    n: str = request.GET.get('number', '').strip()
    x: int = 0
    if n:
        try:
            x = int(n)
        except Exception as e:
            return ResService.error_response('Number %s does not seems to be a valid integer' % n)
    if x <= 0 or x > 100 or int(n) != float(n):
        return ResService.error_response('Required Query Param number should be an Valid Integer between 1 to 100')
    else:
        sols: List[DifferenceSolution] = DifferenceSolution.objects.filter(number=x)
        val: int
        sol: DifferenceSolution
        if sols:
            sol = sols[0]
            val = int(sol.solution)
            sol.occurrence = F('occurrence') + 1
        else:
            val: int = MathService.calculate_difference(x)
            sol = DifferenceSolution(number=x, solution=val)
        sol.save()
        sol.refresh_from_db()

    return ResService.success_response({"id": sol.id, "value": val, "occurrence": sol.occurrence, "number": sol.number,
                                        "datetime": sol.updated.isoformat()})


def pythagorean_triplets(request):
    a: str = request.GET.get('a', '').strip()
    b: str = request.GET.get('b', '').strip()
    c: str = request.GET.get('c', '').strip()

    if not a or not b or not c:
        return ResService.error_response('Required Parameters are a, b, c')

    try:
        MathService.pythagorean_triplet(a, b, c)
        sorted_numbers: List = sorted([int(a), int(b), int(c)])
        val: bool
        sols: List[PythagoreanTripletSolution] = PythagoreanTripletSolution.objects.filter(number_a=sorted_numbers[0],
                                                                                           number_b=sorted_numbers[1],
                                                                                           number_c=sorted_numbers[2])
        sol: PythagoreanTripletSolution
        if sols:
            sol = sols[0]
            val = bool(sol.solution)
            sol.occurrence = F('occurrence') + 1
        else:
            mul, is_triplet = MathService.pythagorean_triplet(a, b, c)
            sol = PythagoreanTripletSolution(number_a=sorted_numbers[0], number_b=sorted_numbers[1],
                                             number_c=sorted_numbers[2], solution=mul, is_triplet=is_triplet)
        sol.save()
        sol.refresh_from_db()

        return ResService.success_response(
            {"id": sol.id,
             "number_a": sol.number_a,
             "number_b": sol.number_b,
             "number_c": sol.number_c,
             "solution": sol.solution,
             "is_triplet": sol.is_triplet,
             "occurrence": sol.occurrence,
             "datetime": sol.updated.isoformat()})

    except Exception as e:
        return ResService.error_response(message=str(e))
