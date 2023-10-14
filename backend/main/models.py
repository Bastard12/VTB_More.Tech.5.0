# -*- coding: windows-1251 -*

from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class atms(models.Model):
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    allDay = models.BooleanField()

    # Поля для служб внутри банкомата
    wheelchair_serviceCapability = models.CharField(max_length=15)
    wheelchair_serviceActivity = models.CharField(max_length=15)
    blind_serviceCapability = models.CharField(max_length=15)
    blind_serviceActivity = models.CharField(max_length=15)
    nfcForBankCards_serviceCapability = models.CharField(max_length=15)
    nfcForBankCards_serviceActivity = models.CharField(max_length=15)
    qrRead_serviceCapability = models.CharField(max_length=15)
    qrRead_serviceActivity = models.CharField(max_length=15)
    supportsUsd_serviceCapability = models.CharField(max_length=15)
    supportsUsd_serviceActivity = models.CharField(max_length=15)
    supportsChargeRub_serviceCapability = models.CharField(max_length=15)
    supportsChargeRub_serviceActivity = models.CharField(max_length=15)
    supportsEur_serviceCapability = models.CharField(max_length=15)
    supportsEur_serviceActivity = models.CharField(max_length=15)
    supportsRub_serviceCapability = models.CharField(max_length=15)
    supportsRub_serviceActivity = models.CharField(max_length=15)


class Offices(models.Model):
    salePointName = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    rko = models.CharField(max_length=250)
    officeType = models.CharField(max_length=50)
    salePointFormat = models.CharField(max_length=50)
    suoAvailability = models.CharField(max_length=50)
    hasRamp = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    metroStation = models.CharField(max_length=255, null=True, blank=True)
    distance = models.IntegerField()
    kep = models.BooleanField()
    myBranch = models.BooleanField()

    # Для юр лиц
    ul_mon = models.CharField(max_length=255)
    ul_tue = models.CharField(max_length=255)
    ul_wen = models.CharField(max_length=255)
    ul_thu = models.CharField(max_length=255)
    ul_fri = models.CharField(max_length=255)
    ul_sat = models.CharField(max_length=255)
    ul_san = models.CharField(max_length=255)

    # Для физ лиц
    fl_mon = models.CharField(max_length=255)
    fl_tue = models.CharField(max_length=255)
    fl_wen = models.CharField(max_length=255)
    fl_thu = models.CharField(max_length=255)
    fl_fri = models.CharField(max_length=255)
    fl_sat = models.CharField(max_length=255)
    fl_san = models.CharField(max_length=255)

    def __str__(self):
        return self.salePointName

