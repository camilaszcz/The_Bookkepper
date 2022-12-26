"""BookKeeper_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib import admin

# Use include() to add URLS from the catalog application and authentication system
# Use static() to add url mapping to serve static files during development (only)

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("" , include("pages.urls")),
    path("admin/", admin.site.urls),
    path('my_library/', include('my_library.urls')),
    # path('currently_reading/', include('my_library.urls')),
    # path('nex_in_line/', include('my_library.urls')),
    path('loans/', include('loans.urls')),
    path("accounts/", include('django.contrib.auth.urls'))
] + static (settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
