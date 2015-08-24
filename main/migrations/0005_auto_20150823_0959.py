# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150823_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speedmodel',
            name='down_votes',
        ),
        migrations.RemoveField(
            model_name='speedmodel',
            name='up_votes',
        ),
    ]
