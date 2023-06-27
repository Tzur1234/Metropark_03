from django import forms
from my_awesome_project.fines.models import Payment, Fine


class PaymentCreationForm(forms.ModelForm):

    # Perform additional validation
    def clean_amount_in_pennies(self):
        amount_in_pennies = self.cleaned_data.get('amount_in_pennies') # How much the user has payed
        fine_object = self.cleaned_data.get('fine')  # the Fine object



        # Set the desired max limit
        max_limit = fine_object.amount_in_pennies
        payments = Payment.objects.filter(fine=fine_object.id) # all history payments

        # calculating the max_limit the user can pay 
        for payment in payments:
            max_limit -= payment.amount_in_pennies
       

        
        if amount_in_pennies and amount_in_pennies > max_limit:
            raise forms.ValidationError("Amount exceeds the maximum limit.")
        return amount_in_pennies


    class Meta:
        model = Payment
        fields = ['fine' ,'type', 'amount_in_pennies']

        # Prevent from the user to chose unwilling fine
        widgets = {
            'fine': forms.HiddenInput(),
        }
       


