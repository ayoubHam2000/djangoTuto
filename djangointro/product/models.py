from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length = 120)
    description = models.TextField(blank = True,  null = True) #null = dataBase; blank = False => required
    price       = models.DecimalField(decimal_places = 2, max_digits = 10000)
    summary     = models.TextField()
    featued     = models.BooleanField(default = True)

    def get_url(self):
        return reverse("products:product_detail", kwargs={"my_id" : self.id})
        #return f"/products/{self.id}"