from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$',
        'nsa.views.index',
        name="nsa_index"),

    url(r'^logon/$',
        'nsa.views.logon',
        name="nsa_logon"),
    url(r'^logoff/$',
        'nsa.views.logoff',
        name="nsa_logoff"),

    url(r'^warrant/$',
        'nsa.views.warrant',
        name="nsa_warrant"),

    url(r'^users/$', 'nsa.views.users',
        name="nsa_users"),
    url(r'^users/(?P<user_id>\d+)?$',
        'nsa.views.users',
        name="nsa_users"),

    url(r'^users/(?P<user_id>\d+)/data?$',
        'nsa.views.users_data',
        name="nsa_users_data"),
    url(r'^users/(?P<user_id>\d+)/data/(?P<data_id>\d+)?$',
        'nsa.views.users_data',
        name="nsa_users_data"),
)
