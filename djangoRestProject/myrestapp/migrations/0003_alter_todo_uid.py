# Generated by Django 3.2.13 on 2022-07-01 09:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myrestapp', '0002_auto_20220630_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('487d6001-3cd6-4c9e-be5c-daac23d2c6c7'), editable=False, primary_key=True, serialize=False),
        ),
    ]
