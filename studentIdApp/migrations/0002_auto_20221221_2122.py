# Generated by Django 3.2.4 on 2022-12-21 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentIdApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='school',
        ),
        migrations.AddField(
            model_name='user',
            name='schoolname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
