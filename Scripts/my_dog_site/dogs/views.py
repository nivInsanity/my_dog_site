from django.http import HttpResponse
from django.template import loader
from .models import Dog

def dogs(request):
    mydogs = Dog.objects.all().values()
    template = loader.get_template('all_dogs.html')
    context = {
        'mydogs': mydogs,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mydog = Dog.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mydog': mydog
    }
    return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
    mydogs = Dog.objects.filter(name="Bob").values()
    template = loader.get_template('template.html')
    context = {
        'mydogs': mydogs,
    }
    return HttpResponse(template.render(context, request))