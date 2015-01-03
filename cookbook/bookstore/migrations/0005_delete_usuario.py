# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_auto_20150103_1723'),
    ]

    operations = [
        migrations.DeleteModel(
            name='usuario',
        ),
    ]
