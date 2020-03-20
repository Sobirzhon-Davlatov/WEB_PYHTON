
from django.conf.urls import url
from main.views import hello,hello2, products_id, hello3, hello4

urlpatterns =[
  url(r'^wow/', hello),
  url(r'^products/', hello2),
  url(r'^wow/<int:product_id>/', products_id),
  url('^hello3/', hello3),
  url('^hello3/<int:id>/', hello4),

]
