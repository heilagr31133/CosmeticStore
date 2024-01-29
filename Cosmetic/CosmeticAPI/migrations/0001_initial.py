# Generated by Django 4.2 on 2023-04-19 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='name')),
                ('phone_number', models.CharField(max_length=15, verbose_name='phone')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, upload_to='media', verbose_name='image')),
                ('product_name', models.CharField(max_length=255, verbose_name='product_name')),
                ('sell', models.IntegerField(default=0, verbose_name='Цена')),
            ],
        ),
    ]