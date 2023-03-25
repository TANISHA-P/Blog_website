from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Post
from .forms import PostCreateForm
# from django.views.generic import ListView

# Create your views here.
def home(request):
    context = {
        'posts' : Post.objects.all().order_by('-date_posted'),
        'title' : 'Home'
    }
    return render(request, 'blog/home.html',context) #All html files must be in templates folder.

# Class based view example for home view
# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/home.html'
#     context_object_name = 'posts'
#     ordering = ['-date_posted']

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})

def detailed_content(request,data):
    post = Post.objects.filter(title = data).first()
    if(post):
        return render(request,'blog/detailed_content.html',{'post': post})
    else:
        return render(request,'blog/no_content.html')

def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            newpost = Post()
            newpost.title = form.cleaned_data.get('title')
            newpost.content = form.cleaned_data.get('content')
            newpost.author = request.user
            newpost.save()
            messages.success(request, f'Post created Successfully!')
            return redirect('blog-home')
        else:
            messages.error(request,f'Error while creating the post')
            return redirect('blog-create')
    else:
        form = PostCreateForm()
        return render(request, 'blog/post_create.html',{'form':form})