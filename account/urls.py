from django.conf.urls import url
from . import views

urlpattern = [
	# post views
	url(r'^login/$', views.user_login, name='login'),
]