# Generated by Django 5.0.2 on 2024-02-15 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallary', '0004_alter_gallaryimage_gallary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallaryimage',
            name='image',
            field=models.FileField(upload_to='gallaries/images'),
        ),
    ]