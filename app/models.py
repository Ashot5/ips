from django.db import models


class User(models.Model):
    """
    Creating User model and his table on postgresql(using Django ORM)
    """
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
