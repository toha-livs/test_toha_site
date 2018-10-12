from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views
import note.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    path('admin/', admin.site.urls),
    path('home/', note.views.home, name='home'),
<<<<<<< HEAD
    path('api_test/', note.views.snippet_list, name='list'),
=======
    path('api_test/', views.snippet_list, name='list'),
>>>>>>> 0e04f7b5a60caef8395d70ab84e5ba4dec71ef51
]
