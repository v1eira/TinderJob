from django.urls import path, re_path
from .views import views

urlpatterns = [
    re_path(r'^$', views.login_user, name='login_user'),
    path('login/submit', views.submit_login, name='submit_login'),
    path('vagas', views.vagas_list, name='vagas_list'),
    # re_path(r'^candidato/<username>/empresas_list/(?P<pk>\d+)/$', views.pre_match_empresas_list, name='pre_match_empresas_list'),
]
