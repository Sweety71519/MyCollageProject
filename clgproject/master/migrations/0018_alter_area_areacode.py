# Generated by Django 4.1.7 on 2023-04-19 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0017_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='areacode',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
