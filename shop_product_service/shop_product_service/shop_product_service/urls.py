from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from shop import urls as shop_url

from rest_framework.documentation import include_docs_urls

API_TITLE = 'PRODUCT SERVICE'
API_DESCRIPTION = 'A Web API Description for PRODUCT SERVICE'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('api/', include(shop_url)),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)