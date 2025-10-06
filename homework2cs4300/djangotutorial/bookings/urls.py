from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import (
    MovieViewSet,
    SeatViewSet,
    BookingViewSet,
    movie_list,
    seat_booking,
    booking_history
)

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)


urlpatterns = [
    path('', views.movie_list, name='movie_list'),  # home page
    path('book/<int:movie_id>/', views.seat_booking, name='seat_booking'),
    path('booking-history/', views.booking_history, name='booking_history'),
]