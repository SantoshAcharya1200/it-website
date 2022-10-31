from django.views import generic
from .models import Post
from django.http import HttpResponse
import random
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from django.db.models import Q


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1,category = 'technology').order_by('created_on')

    template_name = 'blog.html'
    paginate_by = 2

    def get_context_data(self, *args, **kwargs):
        context = super(PostList, self).get_context_data(*args, **kwargs)
        context['posts'] = Post.objects.all()
        return context

class SearchResultView(generic.ListView):
    model = Post
    template_name = 'blog.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Post.objects.filter(
            Q(title__icontains=query)
        )
        return object_list


class MgmtPostList(generic.ListView):
    queryset = Post.objects.filter(status=1,category='management').order_by('created_on')
    template_name = 'management.html'
    paginate_by = 2

    def get_context_data(self, *args, **kwargs):
        context = super(MgmtPostList, self).get_context_data(*args, **kwargs)
        context['posts'] = Post.objects.all()
        return context

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


def mgmt_post_detail(request, slug):
    template_name = 'mgmt_post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})