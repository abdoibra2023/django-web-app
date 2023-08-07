from django.db import models

# Create your models here.

BUY_OPTIONS =(
    ("black","black"),
    ("white","white"),
)

class prod(models.Model):  # ----> table
    seales_name = models.CharField(max_length=100) # -----> column
    description = models.TextField(max_length=1000)
    buy_options = models.CharField(max_length=15,choices=BUY_OPTIONS)
    
    def __str__(self) -> str:
        return self.seales_name