# Generated by Django 3.2.9 on 2021-11-10 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_address_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.customer')),
            ],
        ),
        migrations.AddField(
            model_name='furniture',
            name='cost',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='TicketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0.0)),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('furniture', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.furniture')),
                ('ticket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.ticket')),
            ],
        ),
    ]