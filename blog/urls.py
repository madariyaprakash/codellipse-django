from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name="blog-home"),
    path('blog/<int:id>/<str:slug>/', views.post_detail, name="post-detail"),
    path('blog/post_edit/<int:id>/', views.post_edit, name="post-edit"),
    path('blog/post_delete/<int:id>/', views.post_delete, name="post-delete"),
    path('blog/post_create/', views.post_create, name="post-create"),
    path('blog/post_like/', views.like_post, name="post-like"),
    path('blog/fav_post/', views.fav_post, name="post-favourite"),
    path('blog/favourites/', views.post_favourite_list, name= "post-favourite-list"),
    path('blog/liked/', views.post_liked_list, name= "post_liked_list"),
    # path('blog/most_liked', views.most_liked, name = "most-liked")
    path('ask_question/create/', views.ask_question_create, name='create-ask-question'),
    path('ask_question/<int:id>/<str:slug>/', views.ask_question_detail, name='detail-ask-question'),
    path('ask_question/edit/<int:id>/', views.ask_question_edit, name='edit-ask-question'),
    path('ask_question/delete/<int:id>/', views.ask_question_delete, name='delete-ask-question'),
    path('ask_question/user/all/', views.user_asq_questions, name='all-ask-questions'),
    path('ask_question/all/', views.all_ask_questions, name="all_ask_questions"),
    path('blog/unpublished/posts/', views.user_draft_posts, name="draft-posts"),
    path('ask_question/unpublished/questions/', views.user_draft_questions, name="draft-questions"),
    path('blog/author_profile/', views.post_author_profile, name="post-author-profile"),
    # courses
    path('courses/', TemplateView.as_view(template_name = "courses/courses_page.html"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)