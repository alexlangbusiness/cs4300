# bookings/migrations/0003_rename_bookingdate_to_booked_at.py
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_seat_movie'),  
    ]

    operations = [
        # Rename field bookingDate -> booked_at
        migrations.RenameField(
            model_name='booking',
            old_name='bookingDate',
            new_name='booked_at',
        ),
        # Example: alter user field if needed
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(
                to='auth.User',  # replace with your user model
                on_delete=models.CASCADE,
            ),
        ),
    ]
