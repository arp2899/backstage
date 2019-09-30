from django.http import JsonResponse
from django.shortcuts import render


def difference(request) -> JsonResponse:
    return JsonResponse({"success": True, "data": {"value": 100}})
