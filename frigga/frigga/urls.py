from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('panel/', include('frigga.core.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
