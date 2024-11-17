from django.db import models
from django.contrib.auth.models import User



#create the Brand model:
class Brand(models.Model):
  name = models.CharField(max_length=100,default='')
  instock = models.BooleanField(default=True)
  
  def __str__(self):
    return str(self.name)
  
#create the Category model:
class Category(models.Model):
    catname=models.CharField(max_length=100)

    def __str__(self):
     return str(self.catname)
    

#create the Product model:
class Product(models.Model):
    tital= models.CharField(max_length=100)
    price= models.IntegerField()
    Description= models.TextField(max_length=200)
    img= models.ImageField(upload_to='pics')
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    Discount= models.IntegerField()
    Waranty= models.IntegerField()
    brand= models.ForeignKey(Brand, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.tital) 


#create the ProductImagegallery model:

class ProductImagegallery(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='pics')
    tital=models.CharField(max_length=100)
    description=models.CharField(max_length=200)

    
    def __str__(self):
      return str(self.product.tital)
    
#create the contact_us model:

class contactUs(models.Model):
  name=models.CharField(max_length=200)
  email=models.EmailField(max_length=200)
  subject=models.CharField(max_length=200)
  message=models.TextField(max_length=500)
  data=models.DateTimeField(auto_now_add=True)


  def __str__(self):
      return self.email
   
                                  


class Addtionalinfo(models.Model):
  product=models.ForeignKey(Product, on_delete=models.CASCADE)
  capacity=models.TextField(max_length=2000)
  weight=models.TextField(max_length=2000)
  display=models.TextField(max_length=2000)
  videoRecording=models.TextField(max_length=2000)
  description=models.TextField(max_length=5000)

  def __str__(self):
    return str(self.product.tital)
  


class Cart(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   product=models.ForeignKey(Product,on_delete=models.CASCADE)
   quantity=models.PositiveIntegerField(default=1,null=True,blank=False)
   create_date=models.DateTimeField(auto_now_add=True)


 
class ShippingAddress(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    country=models.CharField(max_length=100,null=True,blank=True)
    areacode=models.CharField(max_length=100)
    primaryphone=models.CharField(max_length=100)
    streetaddress=models.CharField(max_length=255)
    zipcode=models.CharField(max_length=100)
    

class orderplace(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   shippingadres=models.ForeignKey(ShippingAddress,on_delete=models.CASCADE)
   product=models.ForeignKey(Product,on_delete=models.CASCADE)
   quantity=models.PositiveIntegerField(default=1)
   orderDate=models.DateTimeField(auto_now_add=True)

