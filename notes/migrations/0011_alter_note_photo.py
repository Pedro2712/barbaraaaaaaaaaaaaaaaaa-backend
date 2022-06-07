# Generated by Django 4.0.4 on 2022-06-07 12:40

from django.db import migrations, models
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0010_alter_note_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='photo',
            field=models.FileField(null=sqlalchemy.sql.expression.true, upload_to='imagens'),
        ),
    ]
