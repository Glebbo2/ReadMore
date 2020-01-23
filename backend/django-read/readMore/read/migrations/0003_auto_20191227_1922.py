# Generated by Django 2.2.4 on 2019-12-28 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read', '0002_auto_20191217_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='value',
            field=models.IntegerField(choices=[(1, 'Poor'), (2, 'Average'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=1),
        ),
    ]
