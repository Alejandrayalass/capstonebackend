from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(_):
    return HttpResponse("Little Lemon API OK")

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/", include("littlelemonAPI.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path('auth/', include('djoser.urls.authtoken')),
    

]
