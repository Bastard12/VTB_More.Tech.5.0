# Generated by Django 4.2.6 on 2023-10-13 22:08

import json
from django.db import migrations


def load_data_from_json(apps, schema_editor):
    ATMS = apps.get_model('main', 'atms')
    # ���� � JSON ����� � �������
    json_file_path = './data/atms.json'

    # ��������� JSON ���� � ��������� ������
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    # ����������� �� ������ � ������� ������� ������ atms
    for item in data['atms']:
        atms1 = ATMS(
            address=item['address'],
            latitude=item['latitude'],
            longitude=item['longitude'],
            allDay=item['allDay'],
            wheelchair_serviceCapability=item['services']['wheelchair']['serviceCapability'],
            wheelchair_serviceActivity=item['services']['wheelchair']['serviceActivity'],
            blind_serviceCapability=item['services']['blind']['serviceCapability'],
            blind_serviceActivity=item['services']['blind']['serviceActivity'],
            nfcForBankCards_serviceCapability=item['services']['nfcForBankCards']['serviceCapability'],
            nfcForBankCards_serviceActivity=item['services']['nfcForBankCards']['serviceActivity'],
            qrRead_serviceCapability=item['services']['qrRead']['serviceCapability'],
            qrRead_serviceActivity=item['services']['qrRead']['serviceActivity'],
            supportsUsd_serviceCapability=item['services']['supportsUsd']['serviceCapability'],
            supportsUsd_serviceActivity=item['services']['supportsUsd']['serviceActivity'],
            supportsChargeRub_serviceCapability=item['services']['supportsChargeRub']['serviceCapability'],
            supportsChargeRub_serviceActivity=item['services']['supportsChargeRub']['serviceActivity'],
            supportsEur_serviceCapability=item['services']['supportsEur']['serviceCapability'],
            supportsEur_serviceActivity=item['services']['supportsEur']['serviceActivity'],
            supportsRub_serviceCapability=item['services']['supportsRub']['serviceCapability'],
            supportsRub_serviceActivity=item['services']['supportsRub']['serviceActivity']
        )
        atms1.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_offices_openhoursindividual_openhours'),
    ]

    operations = [
        migrations.RunPython(load_data_from_json),
    ]