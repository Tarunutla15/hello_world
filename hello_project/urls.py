from django.contrib import admin
from django.urls import path,include
from mymessage.views import send_hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mymessage.urls')),
]
