from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.contrib.staticfiles.views import serve as serve_static
from django.views.static import serve as serve_media

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

handler404 = 'main.views.page_not_found'

urlpatterns += [
    re_path(r'^static/(?P<path>.*)$', serve_static, {'insecure': True}),
    re_path(r'^media/(?P<path>.*)$', serve_media, {'document_root': settings.MEDIA_ROOT}),
]
