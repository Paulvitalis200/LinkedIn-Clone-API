from django.conf.urls import url
from users import views

urlpattern = [
    url(r'^api/users$', views.users)
]