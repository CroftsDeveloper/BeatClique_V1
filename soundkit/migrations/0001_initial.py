# Generated by Django 5.0.1 on 2024-01-28 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoundKit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(default='soundkit_covers/default.jpg', upload_to='soundkit_covers/')),
                ('sound_file', models.FileField(default='soundkits/default_sound.mp3', upload_to='soundkits/')),
            ],
        ),
    ]
