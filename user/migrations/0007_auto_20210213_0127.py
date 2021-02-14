# Generated by Django 3.1.4 on 2021-02-12 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210211_1804'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0006_auto_20210213_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favs',
            name='fav_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='ürün'),
        ),
        migrations.AlterField(
            model_name='favs',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='kullanıcı'),
        ),
    ]
