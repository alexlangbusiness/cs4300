# Existing REST API viewsets
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

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
    return render(request, 'your_app/movie_list.html', {'movies': movies})

def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(movie=movie)

    if request.method == "POST":
        selected_seats = request.POST.getlist('selected_seats')
        for seat_id in selected_seats:
            seat = Seat.objects.get(id=seat_id)
            seat.is_booked = True
            seat.save()
            Booking.objects.create(user=request.user, movie=movie, seat=seat)
        return redirect('booking_history')

    return render(request, 'your_app/seat_booking.html', {
        'movie': movie,
        'seats': seats
    })

def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'your_app/booking_history.html', {'bookings': bookings})
