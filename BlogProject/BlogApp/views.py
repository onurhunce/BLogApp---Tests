from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Blog, Comment, UserProfile, Friend
from BlogApp.forms import CommentForm, BlogForm, UserForm, FriendForm
from django.contrib import messages
from django.db.models import Q


# -*- coding: utf-8 -*-


def login_required(get_view):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated():
            return get_view(request, *args, **kwargs)
        return render(request, "logout.html")

    return wrapper


def index(request):
    """
    Main page for login and register. Retrieve all blogs too.
    """

    all_blogs = Blog.objects.order_by(
        '-publish_date').prefetch_related('owner')
    if request.user.is_authenticated():
        current_user = UserProfile.objects.get(user=request.user)
        login_value = True
        context = {"all_blogs": all_blogs, "login": login_value,
                   "username": current_user}
        return render(request, "BlogApp/index.html", context)
    else:
        login_value = False
        context = {"all_blogs": all_blogs, "login": login_value}

    return render(request, "BlogApp/index.html", context)


def blogs(request):
    """
    Retrieve all blogs which are exists.
    """
    all_blogs = Blog.objects.order_by(
        '-publish_date').prefetch_related('owner')
    data = {"all_blogs": all_blogs}
    return render(request, "BlogApp/blogs.html", data)


def categories(request):
    """
    Retrieve all categories.
    """
    all_categories = Blog.Category_Choices
    return render(request, "BlogApp/category.html", {
        "all_categories": all_categories
    })


def get_category(request, category):
    """
    Gets current category.
    """
    category_type = Blog.objects.filter(
        category=category).prefetch_related('owner')
    return render(request, "BlogApp/get_category.html", {
        "category_type": category_type})


@login_required
def get_user_by_name(request, username):
    """
    Gets current user with his/her profile information.
    """
    blog_name = Blog.objects.filter(
        owner__slug_name=username).prefetch_related('owner__user')
    user_name = UserProfile.objects.get(slug_name=username)
    friends = Friend.objects.filter(
        Q(friend=user_name.user) | Q(
            added_friend=user_name.user)).prefetch_related('added_friend')

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


def get_date(request, month):
    """
    Gets blogs for the current month.
    """
    blogs_in_current_month = Blog.objects.filter(
        publish_date__month=month).prefetch_related('owner')
    return render(request, "BlogApp/date.html", {
        "dates": blogs_in_current_month
    })


def get_blog_and_comment(request, blog_id):
    """
    Gets current blog page and its comments.
    """
    selected_blog = Blog.objects.prefetch_related('owner').get(id=blog_id)
    if request.method == 'POST':
        form = CommentForm(
            request.POST, initial={'comment_blog': blog_id, 'reply': blog_id})
        if request.user.is_authenticated():
            form = CommentForm(
                request.POST,
                initial={'comment_blog': blog_id, 'reply': blog_id,
                         'comment_mail': request.user.email,
                         'comment_name': request.user})
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/blog/" + blog_id)
    else:
        # if user, there is no need for mail and name.
        if request.user.is_authenticated():
            form = CommentForm(
                initial={'comment_blog': blog_id,
                         'comment_mail': request.user.email,
                         'comment_name': request.user})
        else:
            form = CommentForm(initial={'comment_blog': blog_id})

    # retrieve all comments which belong to current blog.
    all_comments = Comment.objects.filter(
        comment_blog=selected_blog.id).prefetch_related('reply')

    replies = all_comments.filter(
        reply=all_comments).prefetch_related('reply')
    return render(request, "BlogApp/blog.html", {
        'form': form, "selected_blog": selected_blog, "comments": all_comments,
        "replies": replies
    })


@login_required
def create_user(request):
    """
    Create new user without using admin page.
    """
    if request.method == 'POST':
        form = UserForm(
            request.POST, initial={'user': request.user.username})
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/blogs/")
    else:
        form = UserForm(initial={'user': request.user.username})

    return render(request, "BlogApp/create_user.html", {"form": form})


@login_required
def add_blog(request):
    """
    Adding new blog without using admin page. Problem in image adding.
    """
    blog_user = UserProfile.objects.get(
        user__username=request.user.username)
    if request.method == 'POST':
        form = BlogForm(request.POST, initial={'owner': blog_user})
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/blogs/")
        else:
            form.non_field_errors()
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
    current_password = request.user.password
    user_name = request.user.username
    return render(request, "BlogApp/settings.html", {
        "user": user_name, "pass": current_password
    })


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
