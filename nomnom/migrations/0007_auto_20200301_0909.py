# Generated by Django 3.0.1 on 2020-03-01 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nomnom', '0006_auto_20200126_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientset',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredientName', to='nomnom.Ingredient'),
        ),
        migrations.AlterField(
            model_name='ingredientset',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredientsets', to='nomnom.Recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='recipe-images/'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='thumbnail',
            field=models.ImageField(upload_to='recipe-thumbs/'),
        ),
    ]