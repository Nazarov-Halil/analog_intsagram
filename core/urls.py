from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.posts.urls')),
    path('account/', include('allauth.urls')),
    path('', include('apps.tags.urls')),
    path('', include('apps.comments.urls')),
    path('', include('apps.likes.urls'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
