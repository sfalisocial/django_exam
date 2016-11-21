from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name="homepage"),
        url(r'^add$', views.addtravel, name="addtravel"),
        url(r'^destination/(?P<id>\d+)$', views.viewtravel, name="viewtravel"),
        url(r'^join/(?P<id>\d+)$', views.join, name="join"),
        url(r'^submit$', views.submit, name="submit"),
#r means raw text input; actual regex in single quotes;
#carrot ^ means start of string
]
