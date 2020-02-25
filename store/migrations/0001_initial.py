# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('messenger_user_id', models.CharField(unique=True, max_length=30)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(help_text=b'Email address', max_length=254)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(max_length=3, choices=[(b'NEW', b'New Order'), (b'ONC', b'Order On Course'), (b'DEL', b'Order Deleted'), (b'FIN', b'Order Finished'), (b'CLD', b'Order Closed')])),
                ('date', models.DateTimeField()),
                ('payment_method', models.CharField(max_length=4, choices=[(b'CASH', b'Dinero en efectivo'), (b'TERM', b'Datafono')])),
                ('delivery_address', models.TextField(max_length=600)),
                ('subtotal', models.IntegerField()),
                ('shipping_cost', models.IntegerField()),
                ('total_tax', models.IntegerField()),
                ('total_cost', models.IntegerField()),
                ('custumer', models.ForeignKey(to='store.Customer')),
            ],
            options={
                'verbose_name': 'Orden',
                'verbose_name_plural': 'Barrios',
            },
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(to='store.Order')),
            ],
            options={
                'verbose_name': 'Item de Orden',
                'verbose_name_plural': 'Items de ordenes',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length=400)),
                ('image_url', models.TextField(max_length=600)),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('description', models.TextField(max_length=400)),
            ],
            options={
                'verbose_name': 'Categoria de Producto',
                'verbose_name_plural': 'Categorias de productos',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(to='store.ProductCategory'),
        ),
        migrations.AddField(
            model_name='orderitems',
            name='product',
            field=models.ForeignKey(to='store.Product'),
        ),
    ]
