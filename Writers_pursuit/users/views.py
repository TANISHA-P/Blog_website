from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
from .forms import UserUpdateForm,ProfileUpdateForm


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
            return render(request,'users/register.html')
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


def another_person_profile(request, data): #accepting an extra parameter along with request.
    the_other_user = User.objects.filter(username = data).first()
    if(the_other_user):
        print(the_other_user.email)
        return render(request,'users/other_profile.html',{"otheruser":the_other_user})
    else:
        return render(request,'users/no_user.html')