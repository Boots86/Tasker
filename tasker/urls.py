from django.conf.urls import url, include
from django.contrib import admin

from tasks.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('tasks.urls')),
    url(r'^new_group/$', NewGroup.as_view()),
    url(r'^new_card/$', NewCard.as_view()),
    url(r'^del_card/$', delCard),
    url(r'^check_card/$', checkCard),
    url(r'^uncheck_card/$', uncheckCard),
    url(r'^del_group/$', delGroup),
]
