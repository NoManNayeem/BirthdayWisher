from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birthday = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.email}"
