# Generated by Django 3.2.6 on 2022-03-03 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0010_auto_20220303_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='proof_business',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='proof_id',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
