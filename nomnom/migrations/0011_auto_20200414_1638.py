# Generated by Django 3.0.1 on 2020-04-14 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomnom', '0010_auto_20200414_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientset',
            name='amount',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredientset',
            name='unit',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
    ]
