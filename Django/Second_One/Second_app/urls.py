from django.conf.urls import url
from Second_app import views

urlpatterns = [
    url(r'^$',views.help,name='help'),
]
