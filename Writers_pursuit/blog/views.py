from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Post
from .forms import PostCreateForm, PostUpdateForm
from django.contrib.auth.decorators import login_required

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

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            newpost = Post()
            newpost.title = form.cleaned_data.get('title')
            newpost.content = form.cleaned_data.get('content')
            newpost.author = request.user

            already_exist = Post.objects.filter(title = newpost.title).count()
            if already_exist > 0:
                messages.error(request,f'A Post with following title already exists!')
                return redirect('blog-create')
            else:
                newpost.save()
                messages.success(request, f'Post created Successfully!')
                return redirect('blog-detail',newpost.title)
        else:
            messages.error(request,f'Error while creating the post')
            return redirect('blog-create')
    else:
        form = PostCreateForm()
        return render(request, 'blog/post_create.html', {'form':form})
    
@login_required
def post_update(request,data):
    gained_post = Post.objects.get(title = data)
    if gained_post.author != request.user:
        messages.error(request,f'Error')
        return redirect('blog-home')
    elif request.method == "POST":
        form = PostUpdateForm(request.POST)
        # print(form.is_valid())
        
        if form.is_valid():
            updatedpost = Post.objects.get(title = data)
            updatedpost.title = request.POST.get('title')
            updatedpost.content = request.POST.get('content')
            updatedpost.save()
            messages.success(request, f'Post updated Successfully!')
            return redirect('blog-detail',request.POST.get('title'))
        else:
            # print(form.errors)
            messages.error(request,f'Error while updating the post')
            return redirect('blog-update',data)
    else:
        instance1 = Post.objects.get(title = data)
        tempform = PostUpdateForm()
        tempform.fields['title'].initial = instance1.title
        tempform.fields['content'].initial = instance1.content

        return render(request,'blog/post_update.html',{'form':tempform})

@login_required
def post_delete(request,data):
    gained_post = Post.objects.get(title = data)
    if gained_post.author != request.user:
        messages.error(request,f'Error')
        return redirect('blog-home')
    else:
        messages.success(request, f'Post deleted Successfully!')
        gained_post.delete()
        return redirect('blog-home')
