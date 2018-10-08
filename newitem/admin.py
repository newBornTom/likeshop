from django.contrib import admin
from newitem.models import Price, Oldprice, Discount

#admin.site.register(Price)

class PriceAdmin(admin.ModelAdmin):
    """
    Administration object for Book models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of book instances in book view (inlines)
    """
    list_display = ('price',)
    

admin.site.register(Price, PriceAdmin)

class OldpriceAdmin(admin.ModelAdmin):
    """
    Administration object for Book models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of book instances in book view (inlines)
    """
    list_display = ('oldprice',)
    

admin.site.register(Oldprice, OldpriceAdmin)

class DiscountAdmin(admin.ModelAdmin):
    """
    Administration object for Book models. 
    Defines:
     - fields to be displayed in list view (list_display)
     - adds inline addition of book instances in book view (inlines)
    """
    list_display = ('discount',)
    

admin.site.register(Discount, DiscountAdmin)