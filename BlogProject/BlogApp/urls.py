from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^$', views.index, name="index"),
    url(r'^blogs/$', views.blogs, name="blogs"),
    url(r'^blogs/friends/$', views.friend_blog_list, name="friend_blog_list"),
    url(r'^blogs/unfriend/([a-z_-]+)$', views.unfriend, name="unfriend"), 
    url(r'^user/([a-z_-]+)/$', views.get_user_by_name, name="get_name"),
    url(r'^create_user', views.create_user, name="create_user"),
    url(r'^blog/([0-9]+)/$', views.get_blog_and_comment, name="get_blog"),
    url(r'^2015/([0-9]+)/$', views.get_date, name="get_date"),
    url(r'^add_blog', views.add_blog, name="add_blog"),
    url(r'^Categories', views.categories, name="categories"),
    url(r'^Category/([A-Za-z]+)/$', views.get_category, name="get_category"),
    url(r'^logout/$', views.add_blog, name="error"),
    url(r'^settings/$', views.settings, name="settings"),
]
