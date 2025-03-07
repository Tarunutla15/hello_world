from django.contrib import admin
from django.urls import path
from mymessage.views import send_hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', send_hello),
]
