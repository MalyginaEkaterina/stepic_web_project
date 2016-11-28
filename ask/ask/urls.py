"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from qa.views import test, main_page, question_page, popular_questions, ask_page

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', main_page, name = 'main_page'),
    url(r'^login/.*$', test),
    url(r'^signup/.*$', test),
    url(r'^question/(?P<id>[^/]+)/', question_page, name = 'question_page'),
    url(r'^ask/.*$', ask_page, name = 'ask_page'),
    url(r'^popular/.*$', popular_questions, name = 'popular_questions'),
    url(r'^new/.*$', test),
]
