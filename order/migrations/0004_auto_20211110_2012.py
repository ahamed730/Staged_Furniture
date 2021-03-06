# Generated by Django 3.2.9 on 2021-11-10 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_furniture_condition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='furniture',
            name='status',
        ),
        migrations.AddField(
            model_name='furniture',
            name='location',
            field=models.CharField(choices=[('Lodi', 'Lodi')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='furniture',
            name='pcs',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='furniture',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='furniture',
            name='unit_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='sku',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
