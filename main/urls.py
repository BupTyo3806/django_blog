from django.conf.urls import url

from . import auth, views

app_name = 'main'
urlpatterns = [
    url(r'^register/$', auth.RegisterFormView.as_view()),
    url(r'^login/$', auth.LoginFormView.as_view()),
    url(r'^logout/$', auth.LogoutView.as_view()),
    url(r'^$', views.index, name="index"),
    url(r'^create_record_page$', views.create_record_page, name="create_record_page"),
    url(r'^create_record$', views.create_record, name="create_record"),
]
