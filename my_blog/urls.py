"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
   path('account/create/', views.register, name='register'),
    path('account/profile/', views.profile, name='profile'),
    path('account/login/',auth_views.LoginView.as_view(template_name='account/login.html'),name='login'),
    path('account/logout/',auth_views.LogoutView.as_view(template_name='account/logout.html'),name='logout'),

    #password-change
    path('password-change/', 
            auth_views.PasswordChangeView.as_view(template_name='account/password_change.html'),
            name='password_change'
        ),
    path('password-change-done/', 
            auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'),
            name='password_change_done'
        ),

    #password-reset-paths
    path('password-reset/',
            auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), 
            name ='password_reset'
        ),
    path('password-reset-done/',
            auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), 
            name ='password_reset_done'
        ),
    path('password-reset-confirm/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),
            name='password_reset_confirm'
        ),
    path('password-reset-complete/',
            auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
            name='password_reset_complete'
        ),

    path('',include('blog.urls')),

]


# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)