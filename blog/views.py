from django.shortcuts import render, get_object_or_404, Http404
from django.shortcuts import HttpResponse , HttpResponseRedirect, redirect, reverse
from datetime import datetime
from .models import Post, Comment, AskQuestion
from .forms import PostCreateForm, PostEditForm, PostCommentForm, AskQuestionCreateForm, AskQuestionEditForm
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# json response "render to string"
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth.models import User

# Create your views here.
def post_list(request):
    # print(dir(request))   # to print what are the request object have.
    # posts = Post.objects.all()  # This was the default django intial queryset
    # which we have modified in the model named file and create a customer queryset which
    # will only retrieve the published posts
    post_list = Post.objects.filter(status="published")    # we define the ordering in Meta tag model cls
    query = request.GET.get('q')
    # print(query)
    if query:
        post_list = Post.objects.filter(
            Q(title__icontains=query)|
            Q(author__username=query)|
            Q(body__icontains=query)
        )
    
    # pagination logic
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')  # getting the page number ans storing into the page variable
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:    # e.g. ?page=abcd (not integer value) [it will lead to first pgae]
        posts = paginator.page(1)
    except EmptyPage:   # e.g. ?page = 999/0 (not available int value) [lead to last page]
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts, 
    }
    return render(request, 'blog/post_list.html', context)


def post_edit(request, id):
    post = get_object_or_404(Post, id = id)
    # white user try to edit the post through url so this condition will apply 
    # to see if that particulat post belong to logged user or not 
    # if not then it will throw Http404 error
    if post.author != request.user:
        raise Http404()
    # -----    
    if request.method == "POST":
        form = PostEditForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, f"POST: {post.title}, has been updated successfully!")
            return HttpResponseRedirect(reverse("post-detail", args=(post.id, post.slug)))
    else:
        form = PostEditForm(instance=post)
    
    context = {
        'form' : form,
        'post' : post,
    }

    return render(request, 'blog/post_edit.html', context)



def post_delete(request, id):
    post = get_object_or_404(Post, id = id)
    if post.author != request.user:
        raise Http404
    post.delete()
    messages.success(request, f"POST: {post.title}, has been deleted successfully!")
    return redirect('blog-home')


def post_detail(request, id, slug):
    post = get_object_or_404(Post, id = id, slug=slug)
    # we don't want replies to be displayed in the same comment list so assign None to reply
    comments = Comment.objects.filter(post = post, reply=None).order_by('-id')
    is_liked = False
    is_favourite = False
    
    if post.likes.filter(id = request.user.id).exists():
        is_liked = True
    
    if post.favourite.filter(id = request.user.id).exists():
        is_favourite = True

    if request.method == 'POST':
        comment_form = PostCommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            # we're getting the reply id first
            reply_id = request.POST.get('comment_id')
            # print(reply_id)
            # If there is no id then reply object data will be None
            comment_qs = None
            # if that id exist then 
            if reply_id:
                # fetching the data what is in respective reply id
                comment_qs = Comment.objects.get(id = reply_id)
            # adding that to the database by passing the comment_qs as arg of reply object
            comment = Comment.objects.create(post = post, user = request.user, content= content, reply=comment_qs)
            comment.save()
            # return HttpResponseRedirect(reverse("post-detail", args=(post.id, post.slug))
    else:
        comment_form = PostCommentForm()
        
    # else:
    #     comment_form = PostCommentForm()

    context = {
        'post':post,
        'is_liked': is_liked,
        'is_favourite': is_favourite,
        'total_likes': post.total_likes(),
        'comments': comments,
        'comments_count': comments.count(),
        'comment_form' : comment_form,
    }   
    return render(request, 'blog/post_detail.html', context)



def post_create(request):
    # We're working to get the filled data saved in the database
    if request.method  == "POST":
        # banner_form = PostBannerForm(request.POST, request.FILES)
        form = PostCreateForm(request.POST, request.FILES)
        # Note : We need to use the request.FILES, becuase we're working on image upload
        if form.is_valid():
            post = form.save(commit=False)  # author field
            post.author = request.user
            post.save()
            messages.success(request, f"POST: {post.title}, has been created successfully!")
    else:
        # banner_form = PostBannerForm()
        form = PostCreateForm()
    context = {
        'form' : form,
    }
    return render(request, 'blog/post_create.html', context)



# post like function 
@login_required
def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    # post = get_object_or_404(Post, id=request.POST.get('id'))
    # print(request.user)
    if post.likes.filter(id = request.user.id).exists():
        post.likes.remove(request.user)
        return HttpResponseRedirect(reverse('post-detail', args=(post.id, post.slug)))
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    
    # context = {
    #     'post':post,
    #     'is_liked': is_liked,
    #     'total_likes': post.total_likes(),
    # } 

    # if request.is_ajax():
    #     html = render_to_string('blog/like_section.html', context, request=request)
    #     # getting the data in string format and assiging to html
    #     return JsonResponse({'form':html})
    #     # here transleting the data in json format
    return HttpResponseRedirect(reverse("post-detail", args=(post.id, post.slug)))


def post_liked_list(request):
    user = request.user
    liked_posts = user.likes.all()
    context = {
        'liked_posts' :liked_posts
    }
    return render(request, 'blog/post_liked_list.html', context)



def fav_post(request):
    post = get_object_or_404(Post, id= request.POST.get('post_id'))
    if post.favourite.filter(id = request.user.id).exists():
        post.favourite.remove(request.user)
        messages.info(request, f"You have removed this post '{post.title}' from bookmarked.")
        return HttpResponseRedirect(reverse('post-detail', args=(post.id, post.slug)))
        is_favourite = False
    else:
        post.favourite.add(request.user)
        messages.info(request, f"You have added this post '{post.title}' to bookmark.")
        is_favourite = True
    return HttpResponseRedirect(reverse('post-detail', args=(post.id, post.slug)))



def post_favourite_list(request):
    user = request.user
    favourite_posts = user.favourite.all()
    context = {
        'favourite_posts' :favourite_posts
    }
    return render(request, 'blog/post_favourite_list.html', context)

# def post_comment(request):
#     form = PostCommentForm(Post)


# def most_liked(request):
#     pass
@login_required
def ask_question_create(request):
    if request.method == "POST":
        form = AskQuestionCreateForm(request.POST)
        if form.is_valid():
            ques = form.save(commit = False)
            ques.author = request.user
            ques.save()
            messages.success(request, "Question has been asked successfully!")
    else:
        form = AskQuestionCreateForm()
    context={
        'form':form
    }
    return render(request, 'ask_question/ask_question_create.html', context)



def ask_question_detail(request, id, slug):
    quest = get_object_or_404(AskQuestion, id=id, slug=slug)
    context ={
        'quest':quest
    }
    return render(request, "ask_question/ask_question_detail.html", context)



def ask_question_edit(request, id):
    question = get_object_or_404(AskQuestion, id=id)

    if question.author != request.user:
        return Http404

    if request.method == "POST":
        form = AskQuestionEditForm(request.POST or None, instance=question)
        if form.is_valid():
            ques = form.save(commit = False)
            ques.author = request.user
            ques.save()
            messages.success(request, "Question has been edited & published successfully!")
            return redirect('all-ask-questions')  
    else:
        form = AskQuestionEditForm(instance=question)
    context={
        'form':form
    }
    return render(request, 'ask_question/ask_question_edit.html', context)



def ask_question_delete(request, id):
    question = get_object_or_404(AskQuestion, id=id)
    if question.author != request.user:
        return Http404
    question.delete()
    messages.success(request, f"POST: {question.title}, has been deleted successfully!")
    return redirect('all-ask-questions')    



def user_asq_questions(request):
    list_ques_ask = AskQuestion.objects.filter(author = request.user).order_by("-id")
    context = {
        'list_ques_ask' : list_ques_ask,
        'list_ques_ask_count' : list_ques_ask.count
    }
    return render(request, "ask_question/user_ask_questions.html", context)



def all_ask_questions(request):
    all_ques = AskQuestion.objects.all().order_by("-id")
    context = {
        'all_ques' : all_ques,
    }
    return render(request, "ask_question/all_ask_questions.html", context)


# This is for list out unpublished posts
def user_draft_posts(request):
    drafted_posts = Post.objects.filter(author = request.user).filter(status="draft").order_by("-id")
    context={
        'drafted_posts' : drafted_posts,
        'drafted_posts_count' : drafted_posts.count
    }
    return render(request, "blog/user_drafted_post.html", context)



# This is for list out unpublished questions
def user_draft_questions(request):
    drafted_ques = AskQuestion.objects.filter(author = request.user).filter(status="draft").order_by("-id")
    context={
        'drafted_ques' : drafted_ques,
        'drafted_ques_count': drafted_ques.count
    }
    return render(request, "ask_question/user_drafted_questions.html", context)




# Post author profile details 
def post_author_profile(request):
    id = request.POST.get("idno")
    user_posts = Post.objects.filter(author_id = id)
    user_info = User.objects.filter(id = id)
    user_asked_ques = AskQuestion.objects.filter(author_id = id)
    print(id)
    print(user_posts)
    context ={
        'user_posts': user_posts,
        'user_posts_counts': user_posts.count,
        'user_info' : user_info,
        'user_asked_ques': user_asked_ques,
        'user_asked_ques_counts': user_asked_ques.count,
    }
    return render(request, "blog/post_author_profile.html", context)

