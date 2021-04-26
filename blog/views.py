from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def Home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'home',
   }
    return render(request, 'blog/index.html', context)

def main(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'blog/main.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_post']
    paginate_by = 3

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url='/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'blog/About.html', context)