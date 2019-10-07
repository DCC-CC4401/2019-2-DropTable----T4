from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.mail
    # add aditional fields in here
    # pass

