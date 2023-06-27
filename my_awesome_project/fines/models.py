from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class CardIDField(models.IntegerField):
    default_validators = [
        MinValueValidator(100000000),
        MaxValueValidator(999999999)
    ]
    description = "Card ID Number"
    unique=False



STATUS_CHOICES = [
        ('O', 'Open'),
        ('C', 'Close'),
    ]

TYPE_CHOICES = [
        ('1', 'Cash'),
        ('2', 'Credit Card'),
        ('3', 'Check'),
    ]

class Fine(models.Model):
    israeli_id = CardIDField(unique=False)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    description = models.TextField()
    amount_in_pennies = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.pk} | id-card {self.israeli_id}"
    

class Payment(models.Model):
    fine = models.ForeignKey("Fine", on_delete=models.CASCADE, related_name='fines')
    date_created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    amount_in_pennies = models.PositiveIntegerField()



