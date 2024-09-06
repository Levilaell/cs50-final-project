from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import Http404
from .forms import UserRegisterForm

def post_list(request, category_id=None):
    search_query = request.GET.get('search', '')  
    category_id = request.GET.get('category', category_id)  

    posts = Post.objects.all()

    if category_id:
        try:
            category = get_object_or_404(Category, id=category_id)
            posts = posts.filter(category=category)
        except Http404:
            return redirect('post_list')

    if search_query:
        posts = posts.filter(title__icontains=search_query) | posts.filter(body__icontains=search_query)

    categories = Category.objects.all()

    return render(request, 'forum/post_list.html', {
        'posts': posts,
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_id,
    })

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'forum/create_post.html', {'form': form})

@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()  
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'forum/create_comment.html', {'form': form, 'post': post})

def post_detail(request, post_id=None):
    try:
        post = get_object_or_404(Post, id=post_id)
        comments = post.comments.all()
    except Http404:
        return redirect('post_list')
    
    return render(request, 'forum/post_detail.html', {'post': post, 'comments': comments})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'forum/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password=password)
            if user is not None:
                login(request, user)
                return redirect('post_list')
            else:
                form.add_error(None, 'Invalid username or password')

    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('post_list')