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
            return JsonResponse(ResService.error_response('Number %s does not seems to be a valid integer' % n))
    if x <= 0 or x > 100 or int(n) != float(n):
        return JsonResponse(ResService.error_response('Required Query Param number should be an Valid Integer between '
                                                      '1 to 100'), status=400)
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

    return JsonResponse(
        ResService.success_response({"value": val, "occurrence": sol.occurrence, "number": int(sol.problem), "datetime": sol.updated.isoformat()}))
