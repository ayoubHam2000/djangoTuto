from django.db import models

class Cource(models.Model):
    title       = models.CharField(max_length = 120)
    content     = models.TextField()
    active      = models.BooleanField(default = True)

    #def get_absolute_url(self):
    #    return reverse("cources:article_detail", kwargs = {"my_id" : self.id})
