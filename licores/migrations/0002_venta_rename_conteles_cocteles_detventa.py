# Generated by Django 4.0.4 on 2023-03-12 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('licores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('descuento', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, null=True)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
            ],
        ),
        migrations.RenameModel(
            old_name='Conteles',
            new_name='Cocteles',
        ),
        migrations.CreateModel(
            name='DetVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('cant', models.IntegerField(default=0)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licores.cocteles')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licores.venta')),
            ],
        ),
    ]
