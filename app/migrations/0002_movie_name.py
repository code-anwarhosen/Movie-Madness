# Generated by Django 4.2.1 on 2023-05-26 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='name',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
