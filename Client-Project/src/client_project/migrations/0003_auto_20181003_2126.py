# Generated by Django 2.0.8 on 2018-10-03 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('client_project', '0002_articlepage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlepage',
            name='basepage_ptr',
        ),
        migrations.DeleteModel(
            name='ArticlePage',
        ),
    ]