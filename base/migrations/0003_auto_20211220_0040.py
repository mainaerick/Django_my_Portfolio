# Generated by Django 3.1.8 on 2021-12-19 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20211219_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
