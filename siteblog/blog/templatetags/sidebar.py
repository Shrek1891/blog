from django import template

from blog.models import Post, Tag

register = template.Library()


@register.inclusion_tag('blog/popular_posts_tpl.html')
def get_popular_posts(limit=3):
    posts = Post.objects.all().order_by('-views')[:limit]
    return {'posts': posts}


@register.inclusion_tag('blog/tags_tpl.html')
def show_tags():
    tags = Tag.objects.all()
    return {'tags': tags}
