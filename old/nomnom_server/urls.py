"""nomnom_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import include, path
from django.conf.urls import include
from nomnom import views

urlpatterns = [

    path('api-auth/', include('nomnom.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('assets/FontManifest.json', views.fontmanifest, name='fontmanifest'),
    path('assets/AssetManifest.json', views.assetmanifest, name='assetmanifest'),
    path('assets/fonts/MaterialIcons-Regular.ttf',
         views.materialicons, name='materialicons'),
    path('assets/packages/cupertino_icons/assets/CupertinoIcons.ttf',
         views.cupertinoicons, name='cupertinoicons'),
    path('assets/resources/images/nomnomlogo_book_only.png',
         views.logo, name='logo'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
