#Serilizers used to convert models to JSON
#Data then can be returned to clients
#Uses models that have been created 
#Created a serializer for each model

from rest_framework import serializers
from .models import Movie, Seat, Booking

class MovieSerializer(serializers.ModelSerializer):

    class Meta:

        model = Movie
        fields = '__all__'

class SeatSerializer(serializers.ModelSerializer):

    class Meta:

        model = Seat
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):

    class Meta:

        model = Booking
        fields = '__all__'
