# Generated by Django 5.0.7 on 2024-07-18 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutAs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='aboutas/')),
                ('title', models.CharField(max_length=55)),
                ('text', models.TextField()),
                ('network_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logo/')),
                ('background', models.ImageField(upload_to='background/')),
                ('title', models.CharField(max_length=55)),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lacation', models.CharField(max_length=320)),
                ('contact_center', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Feadback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='feadback-user/')),
                ('name', models.CharField(max_length=55)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=32)),
                ('question', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductsMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('all', 'All'), ('category1', 'Category1'), ('catefory2', 'Category2'), ('category3', 'Category3')], default='all', max_length=32)),
                ('image', models.ImageField(upload_to='product-image/')),
                ('name', models.CharField(max_length=55)),
                ('about', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DiscountProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.IntegerField()),
                ('product', models.ManyToManyField(to='main.productsmenu')),
            ],
        ),
    ]
