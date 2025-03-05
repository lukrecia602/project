from django.db import models
from datetime import datetime


class Tranzakciok(models.Model):
    felhasznalonev=models.CharField(max_length=100)
    kuldesdatuma = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    kedvezmenyezettneve=models.CharField(max_length=100, default="")
    kedvezmenyezettszamlaszam = models.IntegerField(default=0)
    elkuldottosszeg=models.FloatField()
    elkuldottdevizanem=models.CharField(max_length=4, default="EUR")
    megjegyzesek=models.TextField(default="")

    def __str__(self):
        return f"{self.felhasznalonev} {self.kuldesdatuma} {self.elkuldottosszeg} {self.elkuldottdevizanem} {self.megjegyzesek}"



class mnb_deviza(models.Model):
    date = models.DateField()
    currency = models.CharField(max_length=10)
    value = models.FloatField()

    def __str__(self):
        return self.currency +" - "+str(self.value)
    class Meta:
        verbose_name_plural="Valuta - Deviza"

class mnb_name(models.Model):
    smallname = models.CharField(max_length=5)
    longname = models.CharField(max_length=50)
    status = models.BooleanField(default=True)  

    def __str__(self):
        return self.longname
    class Meta:
        verbose_name_plural="deviza neve"
