from django import template
from blogmania.models import Post

register = template.Library()

@register.inclusion_tag('blogmania/recent_blog_posts.html')
def recent_blog_posts(num_posts):
    blog_list = Post.objects.all().order_by('-pub_date')[:num_posts]
    return {'blog_list': blog_list}


