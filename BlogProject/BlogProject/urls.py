"""BlogProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('BlogApp.urls', namespace="blog")),

    # User authentication urls
    url(r'^accounts/login/$', 'BlogProject.views.login'),
    url(r'^accounts/auth/$', 'BlogProject.views.auth_view'),
    url(r'^accounts/logout/$', 'BlogProject.views.logout'),
    url(r'^accounts/loggedin/$', 'BlogProject.views.loggedin'),
    url(r'^accounts/invalid/$', 'BlogProject.views.invalid_login'),
    url(r'^accounts/register/$', 'BlogProject.views.register_user'),
    url(r'^accounts/register_success/$',
        'BlogProject.views.register_success'),
    url(r'^accounts/resetpassword/$',
        'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^accounts/resetpassword/passwordsent/$',
        'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^accounts/reset/(?P<uidb64>[0-9A-Za-z]+)/(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    url(r'^accounts/reset/done/$',
        'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^xmpp/', include("xmpp.urls")),
]


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
                            (r'^images/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT}))
