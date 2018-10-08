from django.db import models

class Price(models.Model):
    

    price = models.CharField(max_length=200, help_text="Enter price")
   
    

    def __str__(self):
        
        return self.price

class Oldprice(models.Model):
    
   
    oldprice = models.CharField(max_length=200, help_text="Enter old price")
   

    def __str__(self):
        
        return self.oldprice

class Discount(models.Model):
    
  
    discount = models.CharField(max_length=200, help_text="Enter a discount")

    def __str__(self):
        
        return self.discount
