from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from .models import  post

def home(request):
    context = {
        'posts': post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = post

class PostCreateView(CreateView):
    model = post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
 

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
