# Generated by Django 5.2 on 2025-04-11 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_person_id_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id_count',
            field=models.IntegerField(auto_created=True, max_length=4),
        ),
    ]
