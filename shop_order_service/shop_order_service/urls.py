from django.contrib import admin
from django.urls import path, include
from order import urls as order_urls

from rest_framework.documentation import include_docs_urls

API_TITLE = 'ORDER SERVICE'
API_DESCRIPTION = 'A Web API Description for ORDER SERVICE'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(order_urls)),
    path('', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
]
