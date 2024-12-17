from django.db import models
from django.contrib.auth.models import User


class Klientas(models.Model):
    vardas = models.CharField(max_length=100)
    pavarde = models.CharField(max_length=100)
    imone = models.CharField(max_length=200)
    kontaktai = models.TextField()

    class Meta:
        verbose_name = ('Klientas')
        verbose_name_plural = ('Klientai')

    def __str__(self):
        return f"{self.vardas} {self.pavarde}"


class Darbuotojas(models.Model):
    vardas = models.CharField(max_length=100)
    pavarde = models.CharField(max_length=100)
    pareigos = models.CharField(max_length=100)

    class Meta:
        verbose_name = ('Darbuotojas')
        verbose_name_plural = ('Darbuotojai')

    def __str__(self):
        return f"{self.vardas} {self.pavarde}"


class Darbas(models.Model):
    pavadinimas = models.CharField(max_length=200)
    pastabos = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = ('Darbas')
        verbose_name_plural = ('Darbai')

    def __str__(self):
        return self.pavadinimas


class Saskaita(models.Model):
    israsymo_data = models.DateField()
    suma = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = ('Saskaita')
        verbose_name_plural = ('Saskaitos')

    def __str__(self):
        return f"Sąskaita {self.id} - {self.suma} EUR"


class Projektas(models.Model):
    pavadinimas = models.CharField(max_length=200)
    pradzios_data = models.DateField()
    pabaigos_data = models.DateField()
    klientas = models.ForeignKey(Klientas, on_delete=models.CASCADE)
    vadovas = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    darbuotojai = models.ManyToManyField(Darbuotojas, blank=True)
    darbai = models.ManyToManyField(Darbas, blank=True)
    saskaitos = models.ManyToManyField(Saskaita, blank=True)

    class Meta:
        verbose_name = ('Projektas')
        verbose_name_plural = ('Projektai')

    def __str__(self):
        return self.pavadinimas

