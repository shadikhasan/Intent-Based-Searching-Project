from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, search_view

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('search/', search_view),
]
