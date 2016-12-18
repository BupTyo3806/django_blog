from django.conf.urls import url

from . import auth, views

app_name = 'main'
urlpatterns = [
    url(r'^register/$', auth.RegisterFormView.as_view()),
    url(r'^login/$', auth.LoginFormView.as_view()),
    url(r'^logout/$', auth.LogoutView.as_view()),
    url(r'^$', views.index, name="index"),
]
