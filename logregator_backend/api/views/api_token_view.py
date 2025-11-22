
from django.http import HttpResponse
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from ..models import APIToken
from ..decorators.authenticated import is_authenticated 

@is_authenticated
def get(request, api_token):
    if ("X-Api-Token" in request.headers):
        token = request.headers["X-Api-Token"].split()[1]
        try:
            db_token = APIToken.objects.get(content=token)
            data = serializers.serialize("json", [db_token])
            return HttpResponse(data, status=200)
        except ObjectDoesNotExist:
            return HttpResponse(status=404)
    return HttpResponse(status=404)
    
    