# Generated by Django 5.0.1 on 2024-01-29 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0002_remove_basemodel_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basemodel',
            name='created_at',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='basemodel',
            name='modified_at',
            field=models.DateField(null=True),
        ),
    ]