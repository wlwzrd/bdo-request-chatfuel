# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20181007_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(default=b'NEW', max_length=3, choices=[(b'NEW', b'New Order'), (b'ONC', b'Order On Course'), (b'DEL', b'Order Deleted'), (b'FIN', b'Order Finished'), (b'CLD', b'Order Closed')]),
        ),
    ]
