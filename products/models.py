from django.db import models

# Create your models here.

BUY_OPTIONS_COLOR =(
    ("black","black"),
    ("white","white"),
)

PAYMENT_OP = (
    ("cash","cash"),
    ("credit_card","credit_card"),
)

class prod(models.Model):  # ----> table
    seales_name = models.CharField(max_length=100) # -----> column
    description = models.TextField(max_length=1000)
    buy_options_color = models.CharField(max_length=15,choices=BUY_OPTIONS_COLOR)
    price = models.IntegerField(default=500)
    payment_options = models.CharField(max_length=15,choices=PAYMENT_OP)
    # location
    
    def __str__(self):
        return self.seales_name
    
