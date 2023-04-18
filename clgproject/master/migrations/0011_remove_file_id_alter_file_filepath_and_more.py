# Generated by Django 4.1.7 on 2023-04-09 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0010_file_fileinternal_stock_transport_vehicle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='id',
        ),
        migrations.AlterField(
            model_name='file',
            name='filepath',
            field=models.CharField(blank=True, default='#', max_length=200),
        ),
        migrations.AlterField(
            model_name='file',
            name='menuseq',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='status',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]