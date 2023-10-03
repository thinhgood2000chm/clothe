# Generated by Django 3.0.8 on 2020-11-23 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shirts', '0004_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('PENDING', 'Pending'), ('PLACED', 'Placed'), ('CANCELED', 'Canceled'), ('COMPLETED', 'Completed')], max_length=15)),
                ('payment_method', models.CharField(choices=[('COD', 'Cod'), ('ONLINE', 'Online')], max_length=15)),
                ('shipping_address', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=10)),
                ('total', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(default='FAILED', max_length=15)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('payment_id', models.CharField(max_length=70)),
                ('payment_request_id', models.CharField(max_length=70, unique=True)),
                ('Order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shirts.order')),
            ],
        ),
        migrations.CreateModel(
            name='order_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('Order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shirts.order')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shirts.Sizevariant')),
                ('tshirt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shirts.Tshirt')),
            ],
        ),
    ]
