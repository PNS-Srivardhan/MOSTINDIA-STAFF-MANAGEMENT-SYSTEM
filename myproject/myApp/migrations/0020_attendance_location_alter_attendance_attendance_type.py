# Generated by Django 5.1.2 on 2024-12-19 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0019_staff_advance_amount_staff_income_tax_staff_pf_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attendance_type',
            field=models.CharField(choices=[('Onsite', 'Onsite'), ('Offsite', 'Offsite'), ('WFH', 'Work from Home'), ('Leave', 'Leave'), ('Travel', 'Travel'), ('Others', 'Others'), ('Paid_Leave', 'Paid Leave')], default='', max_length=20),
        ),
    ]
