from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from .models import Post
from django.shortcuts import get_object_or_404
# Create your views here.
'''
def indexView(request):
    context = {'name':'Ali'}
    return render(request, 'index.html', context)
'''

class IndexView(TemplateView):
    '''A class based view to show index page.'''
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Ali'
        context['posts'] = Post.objects.all()
        return context

class RedirectToMaktab(RedirectView):
    url = 'https://maktabkhooneh.com'

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)