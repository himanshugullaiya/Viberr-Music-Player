# Generated by Django 2.2.2 on 2019-08-22 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20190820_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_file',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
