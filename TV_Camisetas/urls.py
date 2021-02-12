
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #Incluimos las urls de las apps
    re_path('',include('applications.producto.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)