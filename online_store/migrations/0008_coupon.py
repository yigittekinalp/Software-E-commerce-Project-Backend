# Generated by Django 3.0.4 on 2020-04-30 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0007_auto_20200430_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('couponId', models.AutoField(primary_key=True, serialize=False)),
                ('discountRate', models.FloatField(null=True)),
                ('couponName', models.CharField(max_length=60, null=True)),
                ('cId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='online_store.Customer')),
            ],
        ),
    ]
