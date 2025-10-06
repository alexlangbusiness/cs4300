#Create 3 models for bookings application
#The 3 are models given
#Each has its own specifications, different fields, and relationships
#Booking uses Foreign Key to combine movie and seat together
#Each returns the most important piece of data

from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):

    title = models.CharField(max_length=500)  # required max_length
    description = models.TextField()
    releaseDate = models.DateField()
    duration = models.IntegerField(help_text="Duration: ")

    def __str__(self):
        return self.title

class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="seats")
    seatNumber = models.CharField(max_length=10)
    currentlyBooked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.seatNumber} - {self.movie.title}"

class Booking(models.Model):
    user = models.CharField(max_length=100)   # <-- NEW: store user name or ID as text
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} booked {self.seat} for {self.movie}"



