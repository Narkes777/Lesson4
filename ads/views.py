import imp
from re import template
from tempfile import TemporaryFile
from django.http import HttpResponse, HttpRequest
from .models import Ad
from django.template import loader

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    template = loader.get_template('index.html')
    ads = Ad.objects.all()
    context = {"ads": ads}
    return HttpResponse(template.render(context, request))


    # result = "Объявления:\n\n"
    # for ad in Ad.objects.all():
    #     result += str(ad.name) + '' + str(ad.content) + '' + str(ad.price) + '\n'
    # return HttpResponse(result, content_type="text/plain; charset=utf-8")