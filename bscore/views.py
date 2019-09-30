import json
from typing import List, Optional

from django.db.models import QuerySet, F
from django.http import JsonResponse
from django.shortcuts import render

from bscore.models import Solution, ProblemTypeEnum
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
        sols: List[Solution] = Solution.objects.filter(problem=x, problem_type=ProblemTypeEnum.DIFFERENCE)
        val: int
        sol: Solution
        if sols:
            sol = sols[0]
            val = int(sol.solution)
            sol.occurrence = F('occurrence') + 1
        else:
            val: int = MathService.calculate_difference(x)
            sol = Solution(problem_type=ProblemTypeEnum.DIFFERENCE, problem=x, solution=val)
        sol.save()
        sol.refresh_from_db()

    return ResService.success_response(
        {"value": val, "occurrence": sol.occurrence, "number": int(sol.problem), "datetime": sol.updated.isoformat()})


def pythagorean_triplets(request):
    a: str = request.GET.get('a', '').strip()
    b: str = request.GET.get('b', '').strip()
    c: str = request.GET.get('c', '').strip()

    if not a or not b or not c:
        return ResService.error_response('Required Parameters are a, b, c')

    try:
        problem = '%s - %s - %s' % (a, b, c)
        val: bool
        sols: List[Solution] = Solution.objects.filter(problem_type=ProblemTypeEnum.PYTHAGOREAN_TRIPLET, problem=problem)
        sol: Solution
        if sols:
            sol = sols[0]
            val = bool(sol.solution)
            sol.occurrence = F('occurrence') + 1
        else:
            val = MathService.is_pythagorean_triplet(a, b, c)
            sol = Solution(problem_type=ProblemTypeEnum.PYTHAGOREAN_TRIPLET, problem=problem, solution='true' if val else '')
        sol.save()
        sol.refresh_from_db()
        numbers: str = str(sol.problem)
        return ResService.success_response({"value": val, "occurrence": sol.occurrence, "numbers": numbers, "datetime": sol.updated.isoformat()})

    except Exception as e:
        return ResService.error_response(message=str(e))
