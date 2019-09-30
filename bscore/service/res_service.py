from typing import Dict, Union

from django.http import JsonResponse


class ResService(object):

    @staticmethod
    def success_response(data: any = {}) -> JsonResponse:
        return JsonResponse({
            "success": True,
            "data": data
        })

    @staticmethod
    def error_response(message: str, status: int = 400) -> JsonResponse:
        return JsonResponse({
            "success": False,
            "message": message
        }, status=status)


