from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
from .forms import UserUpdateForm,ProfileUpdateForm
from blog.models import Post
from django.core.paginator import Paginator

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            curruser = User.objects.get(username = username)
            prof = Profile()
            prof.user = curruser
            prof.save()
            messages.success(request, f'Account Created Succesfully for {username}!')
            return redirect('blog-home')
        else:
            messages.error(request,f'Error while creating Account! Please try again')
            return redirect('users-register')
            # return render(request,'users/register.html')
    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html',{"form":form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user) #we use instance field inside a form when update krna ho existing row in a table. Refer notes.
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Profile has been Updated!')
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user) #instance field se already existing data is loaded in the form.
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request,'users/profile.html', context)


def another_person_profile(request, data, pageno=1): #accepting extra parameters along with request.
    the_other_user = User.objects.filter(username = data).first()
    if(the_other_user):
        their_posts = Post.objects.filter(author = the_other_user).order_by('-date_posted')
        their_posts = Paginator(their_posts,5)

        # print(the_other_user.email)
        info = {
            "otheruser" : the_other_user,
            "posts" : their_posts.get_page(pageno)
        }
        return render(request,'users/other_profile.html',info)
    else:
        return render(request,'users/no_user.html')
    
def search_user(request):
    if request.method == 'POST':
        print(request.POST)
        data = request.POST.get('user_name')
        print(data)
        return redirect("another_user-profile",data=data)
    else:
        return render(request,'blog-home')