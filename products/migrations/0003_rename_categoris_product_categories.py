# Generated by Django 4.2.7 on 2023-12-03 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categoris',
            new_name='categories',
        ),
    ]
