from django import template

register = template.Library()
@register.inclusion_tag("BlogApp/main.html")
def main():
	return {}