# Generated by Django 2.0.4 on 2018-04-05 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hanger', '0002_theword_word'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TheWord',
            new_name='Words',
        ),
    ]
