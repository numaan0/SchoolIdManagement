# Generated by Django 3.2.4 on 2022-12-21 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentIdApp', '0002_auto_20221221_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iddata',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=50)),
                ('father', models.CharField(max_length=30)),
                ('mother', models.CharField(max_length=30)),
                ('phno', models.IntegerField()),
                ('ephno', models.IntegerField()),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='photos')),
                ('role', models.CharField(choices=[('student', 'student'), ('teacher', 'teacher')], default='student', max_length=20)),
                ('schoolname', models.CharField(max_length=50)),
            ],
        ),
    ]
