# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-15 17:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20171015_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shiped_time',
        ),
        migrations.AddField(
            model_name='order',
            name='shipped_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=200, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.PositiveIntegerField(verbose_name='總價'),
        ),
        migrations.AlterField(
            model_name='order',
            name='buyer',
            field=models.CharField(max_length=30, verbose_name='訂購人'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cellphone',
            field=models.CharField(max_length=20, verbose_name='電話'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='order',
            name='ip',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.TextField(blank=True, verbose_name='備註'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(max_length=50, verbose_name='訂單號碼'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_way',
            field=models.CharField(max_length=30, verbose_name='付款方式'),
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.PositiveIntegerField(verbose_name='單價'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='產品'),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='order',
            name='value',
            field=models.PositiveIntegerField(verbose_name='數量'),
        ),
    ]
