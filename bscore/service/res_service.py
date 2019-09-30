from typing import Dict, Union


class ResService(object):

    @staticmethod
    def success_response(data: any = {}) -> Dict[str, Union[bool, dict]]:
        return {
            "success": True,
            "data": data
        }

    @staticmethod
    def error_response(message: str) -> Dict[str, Union[bool, str]]:
        return {
            "success": False,
            "message": message
        }


