# Generated by Django 3.0.8 on 2020-07-20 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_price', models.IntegerField(default=0)),
                ('product_size', models.CharField(max_length=50)),
                ('product_brand', models.CharField(max_length=200)),
                ('product_material', models.CharField(max_length=20)),
                ('product_color', models.CharField(max_length=20)),
                ('product_photo', models.ImageField(upload_to='images/')),
            ],
        ),
    ]