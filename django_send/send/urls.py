from django.conf.urls import url
from .views import home

urlpatterns = [
    url(r'^home', home,name='home'),
]