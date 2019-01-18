from django.conf.urls import url, include
from basic_app import views

app_name = 'basic_app'

urlpatterns = [

    #url(r'^basic_app/', include('basic_app.urls')),
    url(r'^register/$', views.register, name='register'),
    url(r'^userLogin/$', views.userLogin, name='userLogin'),
]