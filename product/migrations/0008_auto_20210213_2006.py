# Generated by Django 3.1.4 on 2021-02-13 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210211_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Sweatshirt', 'Sweatshirt'), ('Kaban*Mont', 'Kaban/Mont'), ('Kazak*Hırka', 'Kazak/Hırka'), ('Pantolon', 'Pantolon'), ('Jeans', 'Jeans'), ('Ceket', 'Ceket'), ('Gömlek', 'Gömlek'), ('Takım_Elbise', 'Takım Elbise'), ('Şort*Kapri', 'Şort/Kapri'), ('Tişört', 'Tişört'), ('İç Giyim*Çorap', 'İç Giyim/Çorap'), ('Elbise', 'Elbise'), ('Tayt', 'Tayt'), ('Plaj_Giyim', 'Plaj Giyim'), ('Çanta*Aksesuar', 'Çanta/Aksesuar'), ('Ayakkabı', 'Ayakkabı')], max_length=30, verbose_name='KATEGORİ'),
        ),
    ]