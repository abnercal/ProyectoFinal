# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_bicicleta_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bicicleta',
            name='imagen',
            field=models.ImageField(blank='True', null=True, upload_to='blog/fotos'),
        ),
    ]
