# Generated by Django 5.0.7 on 2024-07-18 19:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_category_remove_productsmenu_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsmenu',
            name='category',
        ),
        migrations.AddField(
            model_name='productsmenu',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
            preserve_default=False,
        ),
    ]
