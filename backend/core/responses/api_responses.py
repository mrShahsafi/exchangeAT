from rest_framework.response import Response

from .api_messages import MESSAGE_CONTENT_EN

"""
    this content is crated for future use.
    By calling the normalize_response() \
        you could have a structural response

    All response will be returned in a similar style \
        and a exact template will be generate.
"""


def normalize_response(
    detail=None,
    code=200,
    message_tilte=MESSAGE_CONTENT_EN,
    message_content=None,
    data=None,
):
    response = dict()
    print(data)

    response.update(
        {
            "detail": f"{detail}",
            "status": f"{code}",
            "messages": [
                {
                    f"{message_tilte}": f"{message_content}",
                }
            ],
        }
    )

    response.update(
        {"data": data},
    )

    return Response(
        response,
        status=code,
    )


class NormalizeResponseMessageCode:
    def __init__(self):
        self.data = {"extra": {"message_code": []}}

    def add_code(self, code):
        self.data["extra"]["message_code"].append(code)

    @property
    def content(self):
        return self.data
