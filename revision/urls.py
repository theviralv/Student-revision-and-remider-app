"""revision URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from tasks.views import list_view, create_view, todo_view, reminder_view, goto_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from registration.views import home_view, signup_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_view, name='list'),
    path('create/', create_view, name='create'),
    path('todo/', todo_view, name='todo'),
    path('reminder/', reminder_view, name='reminder'),
    path('signup/', signup_view, name='signup'),
    path('goto/', goto_view, name='goto'),
    path('accounts/', include("django.contrib.auth.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)