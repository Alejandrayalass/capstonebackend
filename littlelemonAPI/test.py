# littlelemonAPI/tests.py
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import MenuItem

class MenuTests(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser("admin","a@a.com","pass")
        self.user = User.objects.create_user("jane","j@j.com","pass")
        MenuItem.objects.create(title="Pasta", price="9.99", inventory=5)

    def test_menu_list_public(self):
        url = reverse("menuitem-list")
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
        self.assertGreaterEqual(len(r.data["results"]), 1)

    def test_menu_create_requires_staff(self):
        url = reverse("menuitem-list")
        self.client.login(username="jane", password="pass")
        r = self.client.post(url, {"title":"Soup","price":"5.50","inventory":10})
        self.assertEqual(r.status_code, status.HTTP_403_FORBIDDEN)

class BookingTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user("jane","j@j.com","pass")

    def test_booking_requires_auth(self):
        url = reverse("booking-list")
        r = self.client.get(url)
        self.assertEqual(r.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_booking_as_user(self):
        self.client.login(username="jane", password="pass")
        url = reverse("booking-list")
        payload = {"name":"Jane","guest_count":2,"booking_date":"2030-01-01T20:00:00Z"}
        r = self.client.post(url, payload, format="json")
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
        self.assertEqual(r.data["guest_count"], 2)
