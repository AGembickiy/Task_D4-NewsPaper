from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import View
from django.core.paginator import Paginator
from .models import Post
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'news'
    ordering = ['-date_time_creation']
    paginate_by = 1

class PostDetail(DetailView):
    model = Post
    template_name = 'news/newid.html'
    context_object_name = 'newid'


class Posts(View):

    def get(self, request):
        posts = Post.objects.order_by('-date_time_creation')
        p = Paginator(posts, 1)
        posts = p.get_page(request.GET.get('page', 1))
        data = {'posts': posts, }

        return render(request, 'news/paginator.html', data)


class PostSearch(ListView):
    model = Post
    template_name = 'news/search.html'
    context_object_name = 'search'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)

class PostsForm(ListView):
   model = Post
   template_name = 'news/add.html'
   context_object_name = 'add'
   form_class = PostForm
   paginate_by = 1

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['form'] = PostForm()
       return context

   def post(self, request, *args, **kwargs):
       form = self.form_class(request.POST)
       if form.is_valid():
           form.save()
       return super().get(request, *args, **kwargs)

