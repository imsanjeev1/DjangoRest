# Generated by Django 3.2.13 on 2022-07-01 17:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myrestapp', '0005_auto_20220701_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timingtodo',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
