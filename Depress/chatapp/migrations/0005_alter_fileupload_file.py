# Generated by Django 3.2.3 on 2021-08-10 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0004_auto_20210809_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='file',
            field=models.FileField(upload_to='uploaded_files/'),
        ),
    ]