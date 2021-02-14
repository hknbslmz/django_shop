from django.db import models
from django.db import models
from product.models import Product
# Create your models here.

class Favs(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE,verbose_name="kullanıcı")
    fav_product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="ürün")
    
class İnfos(models.Model):
    user = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="kullanıcı")
    adress_name = models.CharField(max_length=25,null=True)
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    adress = models.CharField(max_length=60)
    tel_no = models.CharField(max_length=25)
    e_mail = models.EmailField(max_length=50)
    country = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    post_code = models.CharField(max_length=25)

