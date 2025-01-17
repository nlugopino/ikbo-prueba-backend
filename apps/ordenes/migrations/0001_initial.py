# Generated by Django 5.1.2 on 2024-10-31 04:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ordenes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_orden', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('fecha_caducidad', models.DateField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordenes_producto', to='producto.producto')),
                ('tipo_orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordenes_tipo_orden', to='ordenes.tipoorden')),
            ],
        ),
    ]
