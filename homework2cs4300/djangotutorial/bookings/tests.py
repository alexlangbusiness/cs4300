#Imports everything needed to do unit/integration testing
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Movie, Seat, Booking
from django.utils import timezone

#Unit testing for each different model
class MovieModelTest(TestCase):

    def setUp(self):
        self.movie = Movie.objects.create(title='Potential Movie', description='Potential movie description')

    def test_movie_str(self):
        self.assertEqual(str(self.movie), 'Potential Movie')

#SeatModelTest
class SeatModelTest(TestCase):

    def setUp(self):

        self.movie = Movie.objects.create(title='Potential Movie', description='Potential movie description')
        self.seat = Seat.objects.create(movie=self.movie, seat_number='A1')

    def test_seat_str(self):
        self.assertEqual(str(self.seat), 'A1')

#BookingModelTest
class BookingModelTest(TestCase):

    def setUp(self):

        self.user = User.objects.create(username='testuser')
        self.movie = Movie.objects.create(title='Test Movie', description='A test movie.')
        self.seat = Seat.objects.create(movie=self.movie, seat_number='A1')
        self.booking = Booking.objects.create(

            user=self.user,
            movie=self.movie,
            seat=self.seat,
            booked_at=timezone.now()

        )

    def test_booking_str(self):
        
        expected_str = f"{self.user} - {self.movie.title} - {self.seat.seat_number}"
        self.assertEqual(str(self.booking), expected_str)
