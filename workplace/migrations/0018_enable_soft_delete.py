# Generated by Django 2.0.2 on 2018-10-19 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workplace', '0017_reservation_cancelation'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalperiod',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='historicalreservation',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='historicaltimeslot',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='historicalworkplace',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='period',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='timeslot',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='workplace',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]
