# Generated by Django 5.1.4 on 2024-12-20 10:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='Comm',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='emp',
            name='Mgr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.emp'),
        ),
        migrations.AlterField(
            model_name='emp',
            name='Sal',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
