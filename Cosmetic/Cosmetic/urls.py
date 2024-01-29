from django.urls import path,re_path
from CosmeticAPI.views import AllViews
from Cosmetic import settings
from django.conf.urls.static import static

urlpatterns = [

    path("", AllViews.home),
    path("catalog/", AllViews.catalog),
    path("contact", AllViews.contact),
    path("karkasson", AllViews.karkasson),
    path("catalog/karkasson", AllViews.karkasson),
    path("catalog/karkasson1", AllViews.karkasson),
    path("catalog/karkasson2", AllViews.karkasson),
    path("catalog/karkasson3", AllViews.karkasson),
    path("catalog/karkasson4", AllViews.karkasson),
    path("catalog/karkasson5", AllViews.karkasson),
    path("karkasson1", AllViews.karkasson1),
    path("karkasson2", AllViews.karkasson2),
    path("karkasson3", AllViews.karkasson3),
    path("karkasson4", AllViews.karkasson4),
    path("karkasson5", AllViews.karkasson5),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
