from django.contrib import admin
from .models import Order, OrderItem

class OrderItemList(admin.TabularInline):
    model = OrderItem
    extra = 1  # Allows admin to add new order items in the order form.

class OrderList(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'address', 'division', 'district',
                    'zip_code', 'payment_method', 'account_no', 'totalbook', 'created', 'updated', 'paid']
    list_filter = ['paid', 'created', 'updated']
    search_fields = ['name', 'email', 'phone']  # Allows searching by name/email/phone
    ordering = ['-created']  # Orders by most recent orders first
    inlines = [OrderItemList]

    class Meta:
        model = Order  # Fixed incorrect "Model" capitalization

admin.site.register(Order, OrderList)
