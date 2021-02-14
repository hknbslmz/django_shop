# Generated by Django 3.1.4 on 2021-02-12 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210211_1804'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0005_auto_20210213_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favs',
            name='fav_product',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='fav', to='product.product'),
        ),
        migrations.AlterField(
            model_name='favs',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='kullanıcı'),
        ),
    ]
