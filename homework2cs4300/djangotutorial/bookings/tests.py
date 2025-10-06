from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Movie, Seat, Booking

# -----------------------------
# Movie model tests
# -----------------------------
class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Inception",
            releaseDate="2010-07-16",
            duration=148
        )

    def test_movie_str(self):
        self.assertEqual(str(self.movie), "Inception")

# -----------------------------
# Seat model tests
# -----------------------------
class SeatModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Inception",
            releaseDate="2010-07-16",
            duration=148
        )
        self.seat = Seat.objects.create(movie=self.movie, seatNumber="A1")

    def test_seat_str(self):
        self.assertEqual(str(self.seat), "A1 - Inception")

# -----------------------------
# Booking model tests
# -----------------------------
class BookingModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Inception",
            releaseDate="2010-07-16",
            duration=148
        )
        self.seat = Seat.objects.create(movie=self.movie, seatNumber="B1")
        self.booking = Booking.objects.create(seat=self.seat, user_name="Alice")

    def test_booking_str(self):
        self.assertEqual(str(self.booking), f"Alice - {self.seat.seatNumber}")

# -----------------------------
# Booking API tests
# -----------------------------
class BookingAPITest(APITestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Inception",
            releaseDate="2010-07-16",
            duration=148
        )
        self.seat = Seat.objects.create(movie=self.movie, seatNumber="C1")

    def test_create_booking(self):
        data = {"seat": self.seat.id, "user_name": "Alice"}
        response = self.client.post("/api/bookings/", data, format="json")
        print(response.data)  # See validation errors if it fails
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_seats(self):
        response = self.client.get("/api/seats/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)

# -----------------------------
# Movie API tests
# -----------------------------
class MovieAPITest(APITestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Inception",
            releaseDate="2010-07-16",
            duration=148
        )

    def test_list_movies(self):
        response = self.client.get("/api/movies/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)
