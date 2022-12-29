from django.urls import path, include
from app.views import PostViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]