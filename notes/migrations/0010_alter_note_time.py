# Generated by Django 4.0.4 on 2022-06-06 13:15

from django.db import migrations, models
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0009_alter_note_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='time',
            field=models.FloatField(null=sqlalchemy.sql.expression.true),
        ),
    ]
