from django.contrib import admin
from my_awesome_project.fines.models import Fine, Payment


class FineAdmin(admin.ModelAdmin):
    # list_display = ['israeli_id', 'date_created', 'status', 'description', 'amount_in_pennies']
    list_display = ['pk', 'status', 'israeli_id', 'amount_in_pennies', 'date_created']
    list_filter = ['status', 'israeli_id']
    search_fields = ['israeli_id']
    ordering = ['-date_created', 'israeli_id']

admin.site.register(Fine, FineAdmin)



class PaymentAdmin(admin.ModelAdmin):
    list_display = ('fine', 'date_created', 'type', 'amount_in_pennies')
    list_filter = ('fine__israeli_id',)  # Enable filtering by fine's israeli_id
    search_fields = ('fine__israeli_id',)  # Enable searching by fine's israeli_id
    ordering = ('fine__id',)  # Order the payments by the related fine

admin.site.register(Payment, PaymentAdmin)