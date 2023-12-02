# Generated by Django 4.2.7 on 2023-12-02 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='title')),
                ('description', models.TextField(blank=True, max_length=50, verbose_name='description')),
                ('avatar', models.ImageField(blank=True, upload_to='categories/', verbose_name='avatar')),
                ('is_enable', models.BooleanField(default=True, verbose_name='is enable')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update time')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='parent')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='title')),
                ('description', models.TextField(blank=True, max_length=50, verbose_name='description')),
                ('avatar', models.ImageField(blank=True, upload_to='products/', verbose_name='avatar')),
                ('is_enable', models.BooleanField(default=True, verbose_name='is enable')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update time')),
                ('categoris', models.ManyToManyField(blank=True, to='products.category', verbose_name='categories')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='title')),
                ('file', models.FileField(upload_to='files/%Y/%m/%d/', verbose_name='file')),
                ('is_enable', models.BooleanField(default=True, verbose_name='is enable')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create time')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='update time')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'file',
                'verbose_name_plural': 'files',
                'db_table': 'files',
            },
        ),
    ]
