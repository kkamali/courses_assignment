from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'submit$', views.submit),
    url(r'remove_question$', views.question),
    url(r'remove$', views.remove)
]
