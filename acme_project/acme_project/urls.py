"""acme_project URL Configuration."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('birthday/', include('birthday.urls')),
    path(
        'login/',
        LoginView.as_view(template_name='registration/login.html'),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='registration/logged_out.html'),
        name='logout'
    ),
    path(
        'password_change/',
        PasswordChangeView.as_view(
            template_name='registration/password_change_form.html'
        ),
        name='password_change'
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(
            template_name='registration/password_change_done.html'
        ),
        name='password_change_done'
    ),
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='registration/password_reset_form.html'
        ),
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
