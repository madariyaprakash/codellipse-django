from django.urls import path, include
from user import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('accounts/login/', views.user_login, name="user-login"),
    path('accounts/register/', views.register, name="user-register"),
    path('accounts/user_logout/', views.user_logout, name="user-logout"),

    # password reset view 
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name="user/password_reset.html"),name="password_reset"),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="user/password_reset_done.html"), name="password_reset_done"),
    path('accounts/password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="user/password_reset_confirm.html"), name="password_reset_confirm"),
    path('accounts/password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name="user/password_reset_complete.html"), name="password_reset_complete"),

    # password chane view 
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name="user/password_change.html"), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name="user/password_change_done.html"), name='password_change_done'),

    # user_profile update
    path('accounts/profile/', views.profile, name="user-profile"),

    # Social login options
    path('oauth/', include('social_django.urls', namespace='social')),

    # user all post
    path('user/all_post/', views.all_post, name="all-post"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)