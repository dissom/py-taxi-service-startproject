# Generated by Django 5.0.3 on 2024-03-20 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0007_alter_car_drivers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="driver",
            name="password",
            field=models.CharField(max_length=99),
        ),
    ]
