
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import emailfunc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('email/', emailfunc),
]
