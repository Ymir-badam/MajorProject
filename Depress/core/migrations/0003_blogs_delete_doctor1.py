# Generated by Django 4.2.3 on 2023-11-11 10:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_doctor1"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blogs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Blog_title", models.TextField(max_length=100)),
                ("Blog_content", models.TextField(max_length=500)),
                ("Blog_author", models.TextField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name="Doctor1",
        ),
    ]
