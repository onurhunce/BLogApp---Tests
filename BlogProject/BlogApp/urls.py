from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^$', views.index_page_with_all_posts, name="index"),
    url(r'^blogs/friends/$', views.friend_blog_list, name="friend_blog_list"),
    url(r'^user/([a-z_-]+)/$', views.get_user_profile_page_and_his_posts,
        name="get_name"),
    url(r'^create_user', views.create_new_user_profile, name="create_user"),
    url(r'^blog/([0-9]+)/$', views.get_post_detail_and_post_comments,
        name="get_blog"),
    url(r'^add_comment/([0-9]+)/$', views.add_comment_to_post,
        name="add_comment"),
    url(r'^add_friend/([a-z_-]+)/$', views.add_as_friend_form,
        name="add_friend"),
    url(r'^2015/([0-9]+)/$', views.get_posts_for_selected_month,
        name="get_date"),
    url(r'^add_blog', views.add_new_post, name="add_new_post"),
    url(r'^Categories', views.categories, name="categories"),
    url(r'^Category/([A-Za-z]+)/$', views.get_posts_in_selected_category,
        name="get_category"),
    url(r'^logout/$', views.add_new_post, name="error"),
    url(r'^settings/$', views.settings, name="settings"),
]
