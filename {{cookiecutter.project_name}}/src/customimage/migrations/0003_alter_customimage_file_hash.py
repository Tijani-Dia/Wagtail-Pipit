# Generated by Django 4.0.4 on 2022-05-25 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customimage', '0002_customimage_file_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customimage',
            name='file_hash',
            field=models.CharField(blank=True, db_index=True, editable=False, max_length=40),
        ),
    ]
