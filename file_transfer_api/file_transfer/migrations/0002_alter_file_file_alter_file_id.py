# Generated by Django 4.2.2 on 2023-06-25 12:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("file_transfer", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="file",
            name="file",
            field=models.FileField(upload_to="files/"),
        ),
        migrations.AlterField(
            model_name="file",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
