
from django.contrib.auth.models import AbstractUser
from django.db import models

# Define role choices
ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('coach', 'Coach'),
    ('agent', 'Agent'),
    ('football_player', 'Football Player'),
]

class CustomUser(AbstractUser):
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='football_player')
    
    # You can add additional fields specific to the roles if needed
