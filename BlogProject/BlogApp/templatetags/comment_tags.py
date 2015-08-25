from django import template
from BlogApp.models import Comment
register = template.Library()


@register.inclusion_tag('BlogApp/comment.html')
def main_comment(blog_id):

    all_comments = Comment.objects.filter(
        comment_blog=blog_id).prefetch_related('reply')

    replies = all_comments.filter(reply=all_comments).prefetch_related('reply')

    return {'comments': all_comments, 'replies': replies}


