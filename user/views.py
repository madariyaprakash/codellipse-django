from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse, redirect
from user.forms import UserLoginForm, UserRegistrationForm, UserUpdateForm
from user.forms import ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile
from blog.models import Post
from django.http import Http404
# Create your views here.

# user login view function 

def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            # authenticating the user
            user = authenticate(username = username, password = password)
            # checking if user is already logged in
            if user:
                if user.is_active: 
                    login(request, user) # pass the request and user authentication object
                    return HttpResponseRedirect(reverse('blog-home'))
                else:
                    messages.warning(request, "user is not active")
            else: 
                messages.warning(request,"It's not valid username and password!")
    else:
        form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'user/user_login.html', context)


def user_logout(request):
    logout(request)
    return redirect('blog-home')


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f"Hey {username}, your account has been created successfully!")
            return redirect('user-login')
    else:
        form = UserRegistrationForm()
    context= {
        'form' : form
    }
    return render(request, "user/register.html", context)


def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated successfully!")
            return redirect('user-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'user/user_profile.html', context)



def all_post(request):
    posts = Post.post_list.filter(author =request.user)
    # if posts.author_id != request.user.id:
        # raise Http404()
    context = {
        'posts':posts,
        'num_posts' : posts.count(),
    }
    return render(request, 'user/all_post.html', context)
