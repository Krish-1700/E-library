from django.contrib import admin
from cart.models import Cart

from cart.models import Order_details
from cart.models import Payment

admin.site.register(Cart)

admin.site.register(Order_details)

admin.site.register(Payment)

