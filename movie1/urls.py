from django.conf.urls import url
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^$', views.index),

    url(r'^(?P<movie_id>[0-9]+)/$', views.details),
]