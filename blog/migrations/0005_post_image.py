# Generated by Django 3.0 on 2019-12-27 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191227_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(default=1, upload_to='static'),
            preserve_default=False,
        ),
    ]
