#Defines which URLs should make use of the viewsets
#

import django.urls 
import rest_framework.routers
import .views

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
