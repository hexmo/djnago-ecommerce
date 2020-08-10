# Generated by Django 3.0.8 on 2020-07-20 07:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminDashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_district', models.CharField(max_length=50)),
                ('address_city', models.CharField(max_length=50)),
                ('address_street', models.CharField(max_length=250)),
                ('address_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminDashboard.Address')),
                ('order_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('order_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminDashboard.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cart_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminDashboard.Product')),
            ],
        ),
    ]