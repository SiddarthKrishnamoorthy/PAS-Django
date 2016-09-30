from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	post_create,

	post_detail,
	post_update,
	post_delete,
	ContactWizard,
	process_form_data,
	)

from accounts.views import (login_view, register_view, logout_view)
from posts.forms import (PostForm1, PostForm2, PostForm3)

urlpatterns = [
	url(r'^$', login_view, name='login'),
	url(r'^list/$', post_list, name='list'),
    url(r'^create/$', post_create),
    url(r'^contact/$', ContactWizard.as_view([PostForm1, PostForm2, PostForm3])),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),

]
