# Existing REST API viewsets
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.contrib.auth.decorators import login_required

# --- API ViewSets ---
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


# --- Template Views (for HTML pages) ---
def movie_list(request):

    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def seat_booking(request, movie_id):
    # Get the movie object
    movie = get_object_or_404(Movie, pk=movie_id)

    # Get seats for this movie
    seats = Seat.objects.filter(movie=movie, currentlyBooked=False)

    if request.method == 'POST':
        seat_id = request.POST.get('seat_id')
        seat = get_object_or_404(Seat, pk=seat_id)
        seat.currentlyBooked = True
        seat.save()

        # Create booking record
        Booking.objects.create(
            movie=movie,
            seat=seat,
            user=request.user
        )

    # Define the context dictionary
    context = {
        'movie': movie,
        'seats': seats
    }

    # Render the template with context
    return render(request, 'bookings/seat_booking.html', context)


def booking_history(request):
    
    bookings = Booking.objects.all()
    context = {'bookings': bookings}
    return render(request, 'bookings/booking_history.html', context)
    