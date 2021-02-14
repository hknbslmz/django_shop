from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
CATEGORY_CHOICES = (
    ('Sweatshirt','Sweatshirt'),
    ('Kaban*Mont', 'Kaban/Mont'),
    ('Kazak*Hırka','Kazak/Hırka'),
    ('Pantolon','Pantolon'),
    ('Jeans','Jeans'),
    ('Ceket','Ceket'),
    ('Gömlek', 'Gömlek'),
    ('Takım_Elbise','Takım Elbise'),
    ('Şort*Kapri','Şort/Kapri'),
    ('Tişört','Tişört'),
    ('İç Giyim*Çorap','İç Giyim/Çorap'),
    ('Elbise','Elbise'),
    ('Tayt','Tayt'),
    ('Plaj_Giyim','Plaj Giyim'),
    ('Canta*Aksesuar', 'Çanta/Aksesuar'),
    ('Ayakkabı','Ayakkabı'),
)
SEX_CATEGORY_CHOICES= (
    ('Erkek','Erkek'),
    ('Kadın', 'Kadın'),
    ('Çocuk','Çocuk'),
    
)
class Product(models.Model):
    seller=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="SATICI")
    name=models.CharField(max_length=50,verbose_name="İSİM")
    sex_category=models.CharField(max_length=60,choices=SEX_CATEGORY_CHOICES,null=True,verbose_name="CİNSİYET")
    price=models.FloatField(verbose_name="FİYAT")
    marka = models.CharField(max_length=50,null=True,verbose_name="MARKA")
    image = models.FileField(null=True,verbose_name="FOTOĞRAF")
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES,verbose_name="KATEGORİ")
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma tarihi")
    rating_total = models.FloatField(null=True,blank=True,verbose_name="ortalama puan")
    rating = models.JSONField(default=dict, null=True,blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-rating_total']

class Cart(models.Model):
    user = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="ALICI")
    cart_product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="malzeme")
    number = models.IntegerField(default=1)  


