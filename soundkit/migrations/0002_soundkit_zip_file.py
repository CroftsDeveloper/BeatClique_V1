# Generated by Django 5.0.1 on 2024-02-03 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soundkit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='soundkit',
            name='zip_file',
            field=models.FileField(blank=True, null=True, upload_to='soundkit_zips/'),
        ),
    ]
