from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from my_awesome_project.fines.models import Fine, Payment
from django.urls import reverse_lazy
from my_awesome_project.fines.forms import PaymentCreationForm
from django.shortcuts import get_object_or_404
from django.contrib import messages



# ----------------------------------------------------------------------

class DashboardView(TemplateView):
    """
    The main task of this view is show 
    user's fines in the dashboard.
    """
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # SELECT * FROM Fine WHERE israeli_id=<X> ORDER BY status;
        # Time Complexity O(n) - n the number of fines in the table
        if self.request.user.is_authenticated:     
            fines = Fine.objects.filter(israeli_id=self.request.user.israeli_id)
            context['fines'] = fines
        return context


class PaymentView(CreateView):
    template_name = 'pages/payment.html'
    form_class = PaymentCreationForm

    def get_context_data(self, **kwargs):

        '''
        Add three attributes to the <home> html page:

        The fine related to the current payment
        The total payment amount of the fine
        The amount of money left to pay
        '''

        context = super().get_context_data(**kwargs)
        fine_pk = self.kwargs['pk']  # Retrieve the Fine primary key (pk) from URL
        
        # SELECT * FROM Fine WHERE pk=<fine_pk>
        # Time Complexity: O(n)
        fine_object = Fine.objects.get(pk=fine_pk) 

        total_amount = fine_object.amount_in_pennies
        max_limit = fine_object.amount_in_pennies

        # Set the desired max limit
        # SELECT * FROM payment WHERE fine_id = <fine_object_id>;
        # Time Complexity: O(n)
        payments = Payment.objects.filter(fine=fine_object.id) # all history payments

        # calculating the max_limit the user can pay 
        for payment in payments:
            max_limit -= payment.amount_in_pennies

        # Add the data to the payment.html template
        context['fine_object'] = fine_object 
        context['max_limit'] = max_limit 
        context['total_amount'] = total_amount  
        return context


    # Initialize the default Fine object
    def get_initial(self):
        initial = super().get_initial()
        fine = get_object_or_404(Fine, pk=self.kwargs['pk'])  # Retrieve the Fine object based on the pk from URL
        initial['fine'] = fine
        return initial
    
     # MESSAGE
    def get_success_url(self):
        messages.success(self.request, 'Payment made successfuly !') # Set the success message
        return reverse_lazy('home') # back to deshboard
