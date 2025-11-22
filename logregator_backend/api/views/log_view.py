from django.http import HttpResponse
from django.core import serializers
from ..models import Log
from ..decorators.authenticated import is_authenticated 
from django.views.decorators.http import require_http_methods
import json

@is_authenticated
def get(request, api_token):
    logs = Log.objects.all()
    data = serializers.serialize("json", logs)
    return HttpResponse(data, status=200)
    

@require_http_methods(["POST"])
@is_authenticated
def post(request, api_token):
    try:
        log = Log(json.loads(request.body), api_token.collector)
        log.save()
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=500)

