from django.shortcuts import render

# blog/views.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View 

class YourSignUpView(View):
    template_name = 'blog/signup.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')  # Redirect to your desired page after signup
        return render(request, self.template_name, {'form': form})

# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm

class YourViews(View):
    @staticmethod
    def post_list(request):
        posts = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
        return render(request, 'blog/post_list.html', {'posts': posts})

    @staticmethod
    def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments = post.comments.all()
        comment_form = CommentForm()
        return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

    @login_required
    def post_new(request):
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_form.html', {'form': form, 'form_title': 'New Post', 'form_action_url': 'post_new'})

    @login_required
    def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_form.html', {'form': form, 'form_title': 'Edit Post', 'form_action_url': 'post_edit'})

    @login_required
    def add_comment(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = CommentForm()
        return render(request, 'blog/comment_form.html', {'form': form})

