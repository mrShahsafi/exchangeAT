from rest_framework.exceptions import APIException, _get_error_details
from rest_framework.status import HTTP_400_BAD_REQUEST


class CustomValidationError(APIException):
    status_code = HTTP_400_BAD_REQUEST
    default_detail = "Invalid input."
    default_code = "invalid"

    def __init__(self, detail=None, code=None):
        if detail is None:
            detail = self.default_detail
        if code is None:
            code = self.default_code

        _get_error_details(detail, code)
