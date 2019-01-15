from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
from .models import Posts,Profile
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from .forms import *
from django.contrib import messages


def post_list(request):
    post=Posts.published.all().order_by("-updated")
    query=request.GET.get("q")
    users = User.objects.all()
    if query:
        post = Posts.published.filter(
        Q(title__icontains=query)|
        Q(author__username=query)|
        Q(body__icontains=query)
        )
    context={'post':post,
             'users':users,
            }
    return render(request,'blog/post_list.html',context)

def post_detail(request,slug,id):
    post=get_object_or_404(Posts,id=id,slug=slug)
    #post = get_object_or_404(Posts, id=request.POST.get('id'))
    is_liked = False
    is_favorite = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    if post.favorite.filter(id=request.user.id).exists():
        is_favorite = True



    context={ 'post': post,
        'is_liked': is_liked,
        'is_favorite': is_favorite,
        'total_likes': post.total_likes(),
       }
    return render(request,'blog/post_detail.html',context)
def like_post(request):
    post=get_object_or_404(Posts,id=request.POST.get('post_id'))
    is_liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked=False
    else:
        post.likes.add(request.user)
        is_liked=True

    return HttpResponseRedirect(post.get_absolute_url())

def contact(request):
    if request.method=='POST':
        form=Contact(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()

    else:
        form=Contact()

    context={'form':form,}

    return render(request,'blog/contact_form.html',context)

def post_create(request):
    if request.method=='POST':
        form=PostCreateForms(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()

    else:
        form=PostCreateForms()

    context={'form':form,}

    return render(request,'blog/post_create.html',context)

def user_login(request):
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
           username=request.POST['username']
           password=request.POST['password']
           user=authenticate(username=username,password=password)
           if user:
               if user.is_active:
                   login(request,user)
                   return HttpResponseRedirect(reverse('post_list'))
               else:
                   return HttpResponseRedirect(reverse('user_login'))
           else:
               return HttpResponseRedirect(reverse('user_login'))
    else:
        form=UserLoginForm()
    context={'form':form,}
    return render(request,'blog/login.html',context)

def user_logout(request):
    logout(request)
    return redirect('user_login')

def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user=form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return  redirect('login')
    else:
        form=UserRegistrationForm()
    context={'form':form,}
    return render(request,'blog/register.html',context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(data=request.POST or None, instance=request.user)
        profile_form = ProfileEditForm(data=request.POST or None, instance=request.user.profile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            print(profile_form)
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse("blog:edit_profile"))
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'blog/editprofile.html', context)

def usersprofile(request):
    post=Posts.published.all().order_by("-updated")
    post1=User.objects.all()
    query=request.GET.get("q")
    if query:
        post = Posts.published.filter(
        Q(title__icontains=query)|
        Q(author__username=query)|
        Q(body__icontains=query)
        )
    context={'post':post,
             'post1':post1,}
    return render(request,'blog/users.html',context)


def post_delete(request,id):
    post = get_object_or_404(Posts,id=id)
    if request.user != post.author:
        raise Http404()
    else:
       post.delete()
       messages.warning(request, 'post has been successfully deleted!')
       return redirect('post_list')

def post_favorite_list(request):
    user = request.user
    favorite_posts = user.favourite.all()
    context = {
        'favorite_posts': favorite_posts,
    }
    return render(request, 'blog/post_favorite.html', context)

def favorite_post(request, id):
    post = get_object_or_404(Posts, id=id)
    if post.favorite.filter(id=request.user.id).exists():
        post.favorite.remove(request.user)
    else:
        post.favorite.add(request.user)
    return HttpResponseRedirect(post.get_absolute_url())

def post_edit(request, id):
    post = get_object_or_404(Posts, id=id)
    if post.author != request.user:
        raise Http404()
    if request.method == "POST":
        form = PostEditForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = PostEditForm(instance=post)

    context = {
    'form': form,
    'post': post,

    }
    return render(request, 'blog/post_edit.html', context)
