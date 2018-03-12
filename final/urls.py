from django.conf.urls import url
from .import views


urlpatterns=[
    url(r'^$',views.post_list,name='post_list'),
    url('new1',views.new1,name='new1'),
    url('Otp',views.Otp,name='Otp'),
    url('login',views.login,name='login'),
    url('authn',views.authn,name='authn'),
    url('ajax/validate_username/', views.validate_username, name='validate_username'),
]