# Generated by Django 3.2.4 on 2023-01-01 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentIdApp', '0009_auto_20221227_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
