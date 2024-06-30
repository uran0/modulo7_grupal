from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.name
    
class ProductType(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.category}: {self.name}"

class Product(models.Model):
    sku = models.IntegerField(unique=True,blank=False,default=0)
    name = models.CharField(max_length=100,null=True)
    price = models.IntegerField(blank=False,default=0)
    product_type = models.ForeignKey(ProductType,on_delete=models.CASCADE,blank=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    description = models.TextField(blank=True)

class ProductImg(models.Model):
    title = models.CharField(max_length=60,null=True)
    img = models.ImageField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=False)