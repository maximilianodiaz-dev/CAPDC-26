from rest_framework.response import Response
from rest_framework.views import exception_handler

from apps.shared.domain import DomainException


def domain_exception_handler(exc, context):
    if isinstance(exc, DomainException):
        return Response(
            {"detail": str(exc), "code": type(exc).__name__},
            status=getattr(exc, "http_status", 400),
        )
    return exception_handler(exc, context)
