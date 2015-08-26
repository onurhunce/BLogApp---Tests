from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Blog, Comment, UserProfile, Friend
from BlogApp.forms import CommentForm, BlogForm, UserForm, FriendForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# -*- coding: utf-8 -*-


def index_page_with_all_posts(request):
    """
    Main page for login and register. Retrieve all blogs too.
    """
    all_blogs = Blog.get_all_blogs()
    if request.user.is_authenticated():
        current_user = UserProfile.objects.get(user=request.user)
        return render(request, "BlogApp/index.html", {"all_blogs": all_blogs,
                                                      "username":
                                                          current_user})

    return render(request, "BlogApp/index.html", {"all_blogs": all_blogs})


def categories(request):
    """
    Retrieve all categories.
    """
    all_categories = Blog.category_choices
    return render(request, "BlogApp/category.html", {
        "all_categories": all_categories
    })


def get_posts_in_selected_category(request, category):
    """
    Gets current category.
    """
    category_type = Blog.objects.filter(
        category=category).select_related('owner')
    return render(request, "BlogApp/get_category.html", {
        "category_type": category_type})


@login_required
def get_user_profile_page_and_his_posts(request, username):
    """
    Gets current user with his/her profile information.
    """
    blog_name = Blog.objects.filter(
        owner__slug_name=username).select_related('owner__user')
    user_name = blog_name[0].owner
    friends = Friend.objects.filter(
        Q(friend=user_name.user) | Q(
            added_friend=user_name.user)).select_related('added_friend')

    if request.method == 'POST':
        form = FriendForm(
            request.POST,
            initial={'friend': request.user, 'added_friend': user_name.user})
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/user/" + username)
        return HttpResponse("You are already friend with each other!")
    else:
        form = FriendForm(
            initial={'friend': request.user, 'added_friend': user_name.user})

    return render(request, "BlogApp/users.html", {'form': form,
                                                  "name": blog_name,
                                                  "friends": friends,
                                                  "username": user_name
                                                  })


def get_friend_list_of_user(request, username):
    blog_name = Blog.objects.filter(owner__slug_name=username).select_related(
        'owner__user')
    user_name = blog_name[0].owner

    if request.method == 'POST':
        form = FriendForm(
            request.POST,
            initial={'friend': request.user, 'added_friend': user_name.user})
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/user/" + username)
        return HttpResponse("You are already friend with each other!")
    else:
        form = FriendForm(
            initial={'friend': request.user, 'added_friend': user_name.user})

    return render(request, "BlogApp/users.html", {"form": form})


def get_posts_for_selected_month(request, month):
    """
    Gets blogs for the current month.
    """
    blogs_in_current_month = Blog.objects.filter(
        publish_date__month=month).select_related('owner')
    return render(request, "BlogApp/date.html", {
        "dates": blogs_in_current_month
    })


def add_comment_to_post(request, post_id):
    if request.method == 'POST':
        form = CommentForm(
            request.POST, initial={'comment_blog': post_id, 'reply': post_id})
        if request.user.is_authenticated():
            form = CommentForm(
                request.POST,
                initial={'comment_blog': post_id, 'reply': post_id,
                         'comment_mail': request.user.email,
                         'comment_name': request.user})
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/blog/" + post_id)
    else:
        # if user, there is no need for mail and name.
        if request.user.is_authenticated():
            form = CommentForm(
                initial={'comment_blog': post_id,
                         'comment_mail': request.user.email,
                         'comment_name': request.user})
        else:
            form = CommentForm(initial={'comment_blog': post_id})

    return form


def get_post_detail_and_post_comments(request, blog_id):
    """
    Gets current blog page and its comments.
    """
    selected_blog = Blog.objects.select_related('owner').get(id=blog_id)

    all_comments = Comment.objects.filter(
        comment_blog=selected_blog.id).select_related('reply')

    replies = all_comments.filter(
        reply=all_comments).select_related('reply')

    return render(request, "BlogApp/blog.html", {
        "selected_blog": selected_blog, "comments": all_comments,
        "replies": replies, "form": add_comment_to_post(request, blog_id)
    })


@login_required
def create_new_user_profile(request):
    """
    Create new user without using admin page.
    """
    if request.method == 'POST':
        form = UserForm(
            request.POST, initial={'user': request.user.username})
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserForm(initial={'user': request.user.username})

    return render(request, "BlogApp/create_user.html", {"form": form})


@login_required
def add_new_post(request):
    """
    Adding new blog without using admin page. Problem in image adding.
    """
    blog_user = UserProfile.objects.get(
        user__username=request.user.username)
    if request.method == 'POST':
        form = BlogForm(request.POST, initial={'owner': blog_user})
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect(request, "BlogApp/add_blog.html")
    else:
        form = BlogForm(initial={'owner': blog_user})
        return render(request, "BlogApp/add_blog.html", {
            'form': form, "owner": blog_user
        })


@login_required
def settings(request):
    """
    Reset Password link and other settings for user.
    """
    messages.add_message(request, messages.INFO, 'Settings Page')
    return render(request, "BlogApp/settings.html")


@login_required
# Reset password via sending e-mail to the user
def change_password(request):
    return render(request, "BlogApp/settings.html",
                  {"user": request.user.username})


@login_required
def friend_blog_list(request):
    """
    Gets user's friends blog only. It doesn't work properly. I couldn't get
    dict objects right.
    """
    my_friend_list = Friend.objects.filter(
        Q(friend=request.user) | Q(added_friend=request.user))
    return render(request, "BlogApp/friend_blog.html", {
        "friend_list": my_friend_list, "all_blog": Blog.objects.all()
    })
