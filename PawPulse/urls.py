from django.contrib import admin

from django.urls import path, include

from django.conf import settings

from django.conf.urls.static import static


# ============================================================
# MAIN URL CONFIGURATION
# ============================================================

urlpatterns = [

    # Django Admin
    path(
        'admin/',
        admin.site.urls
    ),

    # Core application
    path(
        '',
        include('core.urls')
    ),

]


# ============================================================
# MEDIA FILES
# ============================================================

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )