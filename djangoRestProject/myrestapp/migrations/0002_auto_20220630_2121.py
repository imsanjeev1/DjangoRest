# Generated by Django 3.2.13 on 2022-06-30 15:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myrestapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('02d565b8-1304-4c71-b99e-fe110a4e71bf'), editable=False, primary_key=True, serialize=False),
        ),
    ]
