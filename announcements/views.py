from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import ListView,DetailView
from announcements.models import Post

def announcements_list(request):
    post_list = Post.objects.all().order_by("-date")
    paginator = Paginator(post_list,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'announcements/announcements.html', {'posts':posts})


"""def announcement(request):
    post_list = Post.objects.all()
    #paginator = Paginator(post_list,1)
    #page = request.GET.get('page')
    #posts = paginator.get_page(page)
    return render(request, 'announcements/announcements.html', {'posts':post_list})

class PostListView(ListView):
    model = Post
    template_name = 'announcements/announcements.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 1
"""
class PostDetailView(DetailView):
    model = Post
    template_name = 'announcements/post.html'
    context_object_name = 'posts'


