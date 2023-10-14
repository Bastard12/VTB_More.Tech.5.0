from rest_framework import serializers
from .models import atms, Offices


class atmsSerializer(serializers.ModelSerializer):

    class Meta:
        model = atms
        fields = ('address', 'latitude', 'longitude', 'allDay', 'wheelchair_serviceCapability', 'wheelchair_serviceActivity','blind_serviceCapability', 'blind_serviceActivity', 'nfcForBankCards_serviceCapability', 'nfcForBankCards_serviceActivity', 'qrRead_serviceCapability', 'qrRead_serviceActivity', 'supportsUsd_serviceCapability', 'supportsUsd_serviceActivity', 'supportsChargeRub_serviceCapability', 'supportsChargeRub_serviceActivity', 'supportsEur_serviceCapability', 'supportsEur_serviceActivity', 'supportsRub_serviceCapability', 'supportsRub_serviceActivity')


class OfficesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offices
        fields = ('salePointName', 'address', 'status', 'rko', 'officeType', 'salePointFormat', 'suoAvailability', 'hasRamp', 'latitude', 'longitude', 'metroStation', 'distance', 'kep', 'myBranch', 'ul_mon', 'ul_tue', 'ul_wen', 'ul_thu', 'ul_fri', 'ul_sat', 'ul_san', 'fl_mon', 'fl_tue', 'fl_wen', 'fl_thu', 'fl_fri', 'fl_sat', 'fl_san')