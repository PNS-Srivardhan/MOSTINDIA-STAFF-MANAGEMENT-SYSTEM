# Generated by Django 5.0.3 on 2024-10-28 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_alter_attendance_attendance_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='incentive',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
