from django.db import models
import datetime
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from stdimage import StdImageField


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    full_name = models.CharField(max_length=200)
    age = models.IntegerField(blank=True)
    location = models.CharField(max_length=300)
    slug_name = models.SlugField(blank=True)
    profile_pic = StdImageField(
        upload_to='images/profile', blank=True, variations={'thumbnail': (450, 300)})

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.full_name)
        super(UserProfile, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.full_name


class Friend(models.Model):
    friend = models.ForeignKey(User, null=True)
    added_friend = models.ForeignKey(User, related_name="added_friend", null=True)
    friendship_date = models.DateTimeField(
        'friend_date', default=datetime.datetime.now, blank=True)

    class Meta:
        unique_together = ('added_friend', 'friend')

    def __unicode__(self):
        return self.added_friend.userprofile.full_name


class Blog(models.Model):

    category_choices = (

        ('Music', 'Music'),
        ('Sport', 'Sport'),
        ('Fashion', 'Fashion'),
        ('Travel', 'Travel'),
        ('Cinema', 'Cinema'),
        ('Photography', 'Photography'),
        ('Food', 'Food'),
        ('Technology', 'Technology'),
        ('Health', 'Health'),
        ('Education', 'Education'),
        ('Politics', 'Politics'),
        ('Other', 'Other'),
    )

    title = models.CharField(max_length=100)
    body = models.TextField(max_length=2000)
    category = models.CharField(
        max_length=11, choices=category_choices, blank=True)
    publish_date = models.DateTimeField(
        'date published', default=datetime.datetime.now, blank=True,
        null=True)
    owner = models.ForeignKey(UserProfile)
    image = StdImageField(
        upload_to='images/', blank=True, null=True, variations={'thumbnail': (
        750, 400)})

    def __unicode__(self):
        return self.title

    @staticmethod
    def get_all_blogs():
        return Blog.objects.order_by('-publish_date').select_related('owner')


class Comment(models.Model):
    comment_text = models.TextField(max_length=200)
    reply = models.ForeignKey('self', blank=True, null=True)
    comment_blog = models.ForeignKey(Blog, null=True, blank=True)
    comment_mail = models.EmailField()
    comment_name = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return self.comment_text
