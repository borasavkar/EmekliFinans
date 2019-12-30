from django.contrib import admin
from django.urls import path,include
from sayfalar import views as sayfalar_views
from django.conf import settings
from django.conf.urls.static import static
from users import views as users_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('sayfalar.urls')),
    path('',sayfalar_views.home,name='home'),
    path('about/', sayfalar_views.about, name='about'),
    path('basvuru/', sayfalar_views.basvuru, name='basvuru'),
    path('contact/', sayfalar_views.contact, name='contact'),
    path('EmekliyeKredi/', sayfalar_views.EmekliyeKredi, name='EmekliyeKredi'),
    path('ptt_kredi/', sayfalar_views.ptt_kredi, name='ptt_kredi'),
    path('SicilBozuk/', sayfalar_views.SicilBozuk, name='SicilBozuk'),
    path('Documents/KisiselVerilerinKorunmasi.pdf', sayfalar_views.kisisel, name='KisiselVerilerinKorunmasi.pdf'),
    path('posts/', sayfalar_views.posts, name='posts'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', users_views.register, name='register'),
    path('profile/', users_views.profile, name='profile'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password-reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password-reset-done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password-reset-confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password-reset-complete'),


] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
