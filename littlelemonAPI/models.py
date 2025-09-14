# littlelemonAPI/models.py
from django.db import models
from django.contrib.auth import get_user_model

class MenuItem(models.Model):
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): return f"{self.title} (${self.price})"

class Booking(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="bookings")
    name = models.CharField(max_length=120)            # nombre cliente
    guest_count = models.PositiveIntegerField()
    booking_date = models.DateTimeField()              # fecha+hora de reserva
    special_requests = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-booking_date"]
        unique_together = ("booking_date", "name")     # simple colisión

    def __str__(self): return f"{self.name} @ {self.booking_date}"
