from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),# url(polls)に、pollsアプリケーションフォルダのurls.pyが紐づく
    path('admin/', admin.site.urls),
]