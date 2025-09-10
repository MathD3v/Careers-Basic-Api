from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from careers.views import PostViewSet

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'careers', PostViewSet, basename='careers')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
