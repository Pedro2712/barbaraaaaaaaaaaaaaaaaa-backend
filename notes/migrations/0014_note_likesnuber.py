# Generated by Django 4.0.4 on 2022-06-11 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0013_remove_note_likesnuber'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='likesNuber',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
