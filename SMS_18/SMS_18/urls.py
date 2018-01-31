from django.conf.urls import url,include
from django.contrib import admin
#from sms_auth.views import home
from .views import index
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', index, name='index'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^auth/', include('sms_auth.urls', namespace="auth")),
    ]

urlpatterns += [
    url(r'', include('main.urls', namespace="main")),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
