# Generated by Django 3.2.5 on 2021-07-26 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Datos', '0003_alter_empleado_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
