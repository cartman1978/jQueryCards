# Generated by Django 3.2.6 on 2022-02-28 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multiform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentation',
            name='pob',
            field=models.FileField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='documentation',
            name='poi',
            field=models.FileField(upload_to='media'),
        ),
    ]
