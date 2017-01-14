from django.conf.urls import url

from . import auth, views

app_name = 'main'
urlpatterns = [
    url(r'^register/$', auth.RegisterFormView.as_view()),
    url(r'^login/$', auth.LoginFormView.as_view()),
    url(r'^logout/$', auth.LogoutView.as_view()),
    url(r'^$', views.index, name="index"),
    url(r'^record/new$', views.record_new, name="record_new"),
    url(r'^record/(?P<record_id>[0-9]+)$', views.one_record, name='one_record'),
    url(r'^record/search$', views.search_records, name='search_records'),
    url(r'^user/(?P<user_id>[0-9]+)$', views.user_records, name='user_records'),
]
