from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    choices = (
        ('Guitar', 'Guitar'),
        ('Drums', 'Drums'),
        ('Bass', 'Bass'),
        ('Keyboard', 'Keyboard'),
    )
    instrument_type = models.CharField(max_length=100,choices=choices)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
