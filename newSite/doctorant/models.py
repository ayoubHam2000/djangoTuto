from django.db import models

class Doctorant(models.Model):
    nom = models.CharField(max_length = 30)
    prenom = models.CharField(max_length = 30)
    these = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

class Conference(models.Model):
    doctorant = models.ForeignKey(Doctorant, on_delete=models.CASCADE)
    time = models.IntegerField()

    def __str__(self):
        return str(self.time)
    