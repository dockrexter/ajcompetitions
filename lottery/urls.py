from django.contrib import admin
from django.urls import path,include
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


 
# admin.site.login_template= "home/login.html"
urlpatterns = [
    
    path('admin/', include('adminPanel.urls')),
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)