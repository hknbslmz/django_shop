# Generated by Django 3.1.4 on 2021-02-12 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210211_1804'),
        ('user', '0003_auto_20210211_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favs',
            name='fav_product',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]