# Create your views here.
from django.utils import timezone
from django.views import generic

from blogmania.models import Post

class IndexView(generic.ListView):
    template_name = "blogmania/index.html"
    context_object_name = 'blog_posts'

    def get_queryset(self):
        return Post.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')

class DetailView(generic.DetailView):
    template_name = 'blogmania/detail.html'
    model = Post

