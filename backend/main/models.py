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


class Offices(models.Model):
    salePointName = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=15)
    rko = models.CharField(max_length=15)
    officeType = models.CharField(max_length=15)
    salePointFormat = models.CharField(max_length=15)
    suoAvailability = models.CharField(max_length=1)
    hasRamp = models.CharField(max_length=1)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    metroStation = models.CharField(max_length=255, null=True, blank=True)
    distance = models.IntegerField()
    kep = models.BooleanField()
    myBranch = models.BooleanField()

    def __str__(self):
        return self.salePointName


class OpenHours(models.Model):
    office = models.ForeignKey(Offices, on_delete=models.CASCADE)
    days = models.CharField(max_length=10)
    hours = models.CharField(max_length=20)


class OpenHoursIndividual(models.Model):
    office = models.ForeignKey(Offices, on_delete=models.CASCADE)
    days = models.CharField(max_length=10)
    hours = models.CharField(max_length=20)
