from django.db import models
from datetime import datetime

# Create your models here.
class Tranzakciok(models.Model):
    felhasznalonev=models.CharField(max_length=100)
    kuldesdatuma = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    kedvezmenyezettneve=models.CharField(max_length=100, default="")
    kedvezmenyezettszamlaszam = models.IntegerField(default=0)
    elkuldottosszeg=models.FloatField()
    elkuldottdevizanem=models.CharField(max_length=4)
    megjegyzesek=models.TextField(default="")

    def __str__(self):
        return f"{self.felhasznalonev} {self.kuldesdatuma} {self.elkuldottosszeg} {self.elkuldottdevizanem} {self.megjegyzesek}"
    
class mnb_deviza(models.Model):
    date = models.DateField() 
    value = models.FloatField()
    currency = models.CharField(max_length=10) #ez tartalmazza az aktuális árfolyamot forintba

    def __str__(self):
        return f"{self.date} {self.currency} {self.value}"
    
    class Meta:
        verbose_name_plural="MNBDeviza"

class mnb_name_good(models.Model):
    currency = models.CharField(max_length=10)
    longname = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.longname}"
        
    class Meta:
        verbose_name_plural="Deviza nevek"

class mnb_name(models.Model):
    smallname = models.CharField(max_length=5)
    longname = models.CharField(max_length=50)

    def __str__(self):
        return self.longname
    class Meta:
        verbose_name_plural="deviza neve"
