from django.contrib import admin
from .models import Brand,Category,Product,ProductImagegallery,contactUs,Addtionalinfo,Cart,ShippingAddress,orderplace

# Register your models here.


## We are Register Brand Model 
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display=("id","name", "instock")

## We are Register Category Model 
@admin.register(Category)
class BrandAdmin(admin.ModelAdmin):
    list_display=("id","catname")
    


## We are Register Product Model 
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=("id","tital","price","Description","img","category","Discount","Waranty","brand")


@admin.register(ProductImagegallery)
class proimageAdmin(admin.ModelAdmin):
    list_display=('id','product','image','tital','description')


@admin.register(contactUs)
class contactAdmin(admin.ModelAdmin):
    list_display=('id','name','email','subject','message','data')

@admin.register(Addtionalinfo)
class AddtionalAdmin(admin.ModelAdmin):
    list_display=('id','product','capacity','weight','display','videoRecording','description')


@admin.register(Cart)
class cartAdmin(admin.ModelAdmin):
    list_display=('id','user','product','quantity','create_date')



@admin.register(ShippingAddress)
class shippingAdmin(admin.ModelAdmin):
    list_display=("id","user","firstname","lastname","country","areacode","primaryphone","streetaddress","zipcode")



@admin.register(orderplace)
class orderAdmin(admin.ModelAdmin):
    list_display=('id','user','shippingadres','product','quantity','orderDate')