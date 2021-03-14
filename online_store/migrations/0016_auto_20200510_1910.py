# Generated by Django 3.0.4 on 2020-05-10 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0015_auto_20200510_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmanager',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='productmanager', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='salesmanager',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='salesmanager', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]