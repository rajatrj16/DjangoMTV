from django.shortcuts import render
from django.http import HttpResponse
from First_app.models import Topic,Webpage,AccessRecord
# Create your views here.
def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record':webpage_list}
    # my_dict = {'insert_me':"Now I am coming from First_app/index.html"}
    # return render(request,'First_app/index.html',context=my_dict)
    return render(request,'First_app/index.html',context=date_dict)
