from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save


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

    def get_status_description(self):
        payment_types = dict(STATUS_CHOICES)
        return payment_types.get(self.status, 'Unknown')

    def __str__(self):
        return f"fineID: {self.pk} | israeli_id {self.israeli_id}"
    

class Payment(models.Model):
    fine = models.ForeignKey("Fine", on_delete=models.CASCADE, related_name='payments')
    date_created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    amount_in_pennies = models.PositiveIntegerField()

    def get_type_description(self):
        payment_types = dict(TYPE_CHOICES)
        return payment_types.get(self.type, 'Unknown')





# When the payment created ...
def post_save_payment_receiver(sender, instance, created, *args, **kwargs):
    if created:
        # get the fine_object
        fine_object = instance.fine
        
        
        # calculating the total history payments
        payments = Payment.objects.filter(fine=fine_object.id) # all history payments
        total_history_payments = 0
        for payment in payments:
            total_history_payments += payment.amount_in_pennies
        
        
        # check if the user has payed all the debt
        if total_history_payments >= fine_object.amount_in_pennies:
            # Update fine status
            fine_object.status = 'C'
            fine_object.save()


# Signals
post_save.connect(post_save_payment_receiver,sender=Payment)



