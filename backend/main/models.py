from django.db import models

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

    def __str__(self):
        return self.address