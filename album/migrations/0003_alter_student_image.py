# Generated by Django 4.0.2 on 2022-02-07 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_rename_post_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]