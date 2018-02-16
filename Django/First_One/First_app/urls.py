from django.conf.urls import url
from First_app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
]
