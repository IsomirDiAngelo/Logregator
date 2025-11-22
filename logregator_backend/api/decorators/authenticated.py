from functools import wraps
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from ..models import APIToken

def is_authenticated(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if ("X-Api-Token" in request.headers):
            split_bearer_token = request.headers["X-Api-Token"].split()
            if (len(split_bearer_token) == 2 and split_bearer_token[0] == "Bearer"):
                bearer_token = split_bearer_token[1]
                try:
                    api_token = APIToken.objects.get(content=bearer_token)
                    return function(request, api_token, *args, **kwargs)
                except ObjectDoesNotExist:
                    return HttpResponse(status=401)
        return HttpResponse(status=401)
    return wrap