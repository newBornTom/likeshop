from django.shortcuts import render
from .models import Price, Oldprice, Discount

def index(request):
    
    for prices in list(Price.objects.all()):
    	price = prices

    for oldprices in list(Oldprice.objects.all()):
    	oldprice = oldprices

    for discounts in list(Discount.objects.all()):
    	discount = discounts
  
    
    
    context = {
        'price': price,
        'oldprice': oldprice,
        'discount': discount,
        
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)






    