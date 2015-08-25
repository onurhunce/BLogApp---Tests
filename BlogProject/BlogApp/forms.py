from django import forms
from django.forms import ModelForm, Textarea
from BlogApp.models import Comment, Blog, UserProfile, Friend
from django.utils.translation import ugettext
from stdimage import StdImageField


class CommentForm(ModelForm):
    comment_blog = forms.ModelChoiceField(queryset=Blog.objects.all(),
                                          widget=forms.HiddenInput())

    class Meta:
        model = Comment
        # exclude = ['reply']
        fields = ['comment_text', 'comment_blog',
                  'reply', 'comment_name', 'comment_mail']
        widgets = {
            'comment_text': Textarea(attrs={'cols': 40, 'rows': 4}),
        }


class UserForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['profile_pic']


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = (
            'title', 'body', 'publish_date', 'owner', 'category', 'image')
        # fields = '__all__'


class FriendForm(ModelForm):
    class Meta:
        model = Friend
        fields = ('friend', 'added_friend', 'friendship_date')
