from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from imageapp.views import ImageViewSet

router = DefaultRouter()
router.register('images', ImageViewSet)
# router.register(r'images/id/resize', ResizeImageView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('images/<int:pk>/resize/', ResizeImageView.as_view()),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
