# littlelemonAPI/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, BookingViewSet  # ← importa los ViewSets correctos
from djoser.views import UserViewSet

router = DefaultRouter()
router.register(r"menuitems", MenuItemViewSet, basename="menuitem")
router.register(r"bookings",  BookingViewSet,  basename="booking")

urlpatterns = [
    path("", include(router.urls)),
    path('api/registro/', UserViewSet.as_view({'post':'create'}), name='registro'),
]
