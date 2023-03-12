# Generated by Django 4.0.4 on 2023-03-12 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conteles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del coctel')),
                ('tags', models.CharField(max_length=100, verbose_name='Tags o palabras claves')),
                ('instrucciones', models.CharField(max_length=200, verbose_name='Instrucciones')),
                ('datos_Glass', models.CharField(max_length=50, verbose_name='Datos del vaso o de la copa')),
                ('category', models.CharField(max_length=45, verbose_name='Categoria')),
            ],
        ),
    ]
