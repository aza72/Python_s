from httplib import HTTPResponse

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'send/base.html')

#123