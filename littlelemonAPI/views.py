# littlelemonAPI/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer, UserRegisterSerializer
from .permissions import IsAdminOrReadOnly

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all().order_by("-updated_at")
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminOrReadOnly]

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        # cada user ve sus reservas; staff ve todas
        if self.request.user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@api_view(["POST"])
def register(request):
    s = UserRegisterSerializer(data=request.data)
    s.is_valid(raise_exception=True)
    s.save()
    return Response({"message":"user created"}, status=status.HTTP_201_CREATED)
