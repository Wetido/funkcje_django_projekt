# Generated by Django 2.2.5 on 2019-09-19 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webpage',
            name='topic',
        ),
        migrations.DeleteModel(
            name='AccessRecord',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.DeleteModel(
            name='Webpage',
        ),
    ]
