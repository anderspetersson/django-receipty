# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business', '0002_auto_20150120_0609'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('amount', models.PositiveIntegerField()),
                ('prize_each', models.DecimalField(max_digits=10, decimal_places=2)),
                ('prize_total', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('prize_total', models.DecimalField(max_digits=10, decimal_places=2)),
                ('account', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('cc_used', models.ForeignKey(to='businessquiz.CreditCard')),
            ],
            options={
                'ordering': ('-pk',),
            },
        ),
        migrations.AddField(
            model_name='item',
            name='receipt',
            field=models.ForeignKey(to='receipt.Receipt'),
        ),
    ]
