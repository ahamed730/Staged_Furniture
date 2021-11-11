# Generated by Django 3.2.9 on 2021-11-11 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20211111_2015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticketitem',
            options={'verbose_name': 'Ticket Item', 'verbose_name_plural': 'Ticket Items'},
        ),
        migrations.AlterField(
            model_name='furniture',
            name='item',
            field=models.CharField(blank=True, choices=[('Sofa & Loveseat', 'Sofa & Loveseat'), ('Sectionals', 'Sectionals'), ('Sofa', 'Sofa'), ('Loveseat', 'Loveseat'), ('Recliner', 'Recliner'), ('Chair', 'Chair'), ('Coffee Table', 'Coffee Table'), ('End Table', 'End Table'), ('Ottoman', 'Ottoman'), ('TV Console', 'TV Console'), ('Fireplaces', 'Fireplaces'), ('Office Desks', 'Office Desks'), ('Office Chairs', 'Office Chairs'), ('Bookcases', 'Bookcases'), ('File Cabinets', 'File Cabinets'), ('Twin Bed', 'Twin Bed'), ('Queen Bed', 'Queen Bed'), ('King Bed', 'King Bed'), ('Dresser', 'Dresser'), ('Nightstand', 'Nightstand'), ('Chest', 'Chest'), ('Twin Mattress', 'Twin Mattress'), ('Full Mattress', 'Full Mattress'), ('Queen Mattress', 'Queen Mattress'), ('King Mattress', 'King Mattress'), ('Adjustable Base', 'Adjustable Base'), ('Box Spring', 'Box Spring'), ('Counter Height Set', 'Counter Height Set'), ('Dining Set', 'Dining Set'), ('Table', 'Table'), ('Dining Chairs', 'Dining Chairs'), ('Bar Height Stools', 'Bar height Stools'), ('Counter Height Stools', 'Counter Height Stools'), ('Island', 'Island'), ('China/Buffet', 'China/Buffet')], max_length=1000, null=True, verbose_name=[('Sofa & Loveseat', 'Sofa & Loveseat'), ('Sectionals', 'Sectionals'), ('Sofa', 'Sofa'), ('Loveseat', 'Loveseat'), ('Recliner', 'Recliner'), ('Chair', 'Chair'), ('Coffee Table', 'Coffee Table'), ('End Table', 'End Table'), ('Ottoman', 'Ottoman'), ('TV Console', 'TV Console'), ('Fireplaces', 'Fireplaces'), ('Office Desks', 'Office Desks'), ('Office Chairs', 'Office Chairs'), ('Bookcases', 'Bookcases'), ('File Cabinets', 'File Cabinets'), ('Twin Bed', 'Twin Bed'), ('Queen Bed', 'Queen Bed'), ('King Bed', 'King Bed'), ('Dresser', 'Dresser'), ('Nightstand', 'Nightstand'), ('Chest', 'Chest'), ('Twin Mattress', 'Twin Mattress'), ('Full Mattress', 'Full Mattress'), ('Queen Mattress', 'Queen Mattress'), ('King Mattress', 'King Mattress'), ('Adjustable Base', 'Adjustable Base'), ('Box Spring', 'Box Spring'), ('Counter Height Set', 'Counter Height Set'), ('Dining Set', 'Dining Set'), ('Table', 'Table'), ('Dining Chairs', 'Dining Chairs'), ('Bar Height Stools', 'Bar height Stools'), ('Counter Height Stools', 'Counter Height Stools'), ('Island', 'Island'), ('China/Buffet', 'China/Buffet')]),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='location',
            field=models.CharField(choices=[('Lodi', 'Lodi')], default='Lodi', max_length=100, null=True, verbose_name=[('Lodi', 'Lodi')]),
        ),
    ]
