# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20181015_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='custumer',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.CharField(default=b'0', max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(default=b'CASH', max_length=4, choices=[(b'CASH', b'Dinero en efectivo'), (b'TERM', b'Datafono')]),
        ),
    ]
