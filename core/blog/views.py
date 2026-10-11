from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post

# Create your views here.

def indexView(request):
    context = {'name':'Ali'}
    return render(request, 'index.html', context)


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Ali'
        context['posts'] = Post.objects.all()
        return context