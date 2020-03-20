from django.http.request import HttpRequest

from django.http.response import HttpResponse


def hello(request):
  return HttpResponse('hello')


def hello2(request):
  return HttpResponse('hello2')


def hello3(request):
  return HttpResponse('fuckbu')


def hello4(request,id):
  return HttpResponse( 'hello worls : {id}')


def products_id(request,product_id):
  return HttpResponse(product_id)

def hello1(request ,product_id):
  return HttpResponse('hello2:',{product_id})


#
# def hello1(request, product_id):
#   return HttpResponse("hello:"+product_id)
