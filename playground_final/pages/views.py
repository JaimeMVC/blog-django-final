from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post
from .models import Author, Comment  

# Vistas de páginas informativas
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Vistas del blog
class PostListView(ListView):
    model = Post
    template_name = 'pages/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all().order_by('-created_at')
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'pages/post_form.html'
    fields = ['title', 'subtitle', 'content', 'image']
    success_url = reverse_lazy('post_list')

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'pages/post_form.html'
    fields = ['title', 'subtitle', 'content', 'image']
    success_url = reverse_lazy('post_list')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'pages/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

# ---------- VISTAS PARA AUTORES ----------

class AuthorListView(ListView):
    model = Author
    template_name = 'pages/author_list.html'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'pages/author_detail.html'

class AuthorCreateView(CreateView):
    model = Author
    fields = ['bio']
    template_name = 'pages/author_form.html'
    success_url = reverse_lazy('author_list')
