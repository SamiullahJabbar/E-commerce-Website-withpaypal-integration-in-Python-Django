from django.shortcuts import render,redirect
from .models import Brand,Category,Product,ProductImagegallery,contactUs,Addtionalinfo,Cart,ShippingAddress,orderplace
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .foam import shipping

# Create your views here.


def index(request):
    all_product = Product.objects.all()
    mob = Product.objects.filter(category__catname ='Mobile')
    tab = Product.objects.filter(category__catname ='Tablet')
    # We are get all catrgory and render in templates
    brand=Brand.objects.all()
    context = {
        'all_product': all_product,
        'mobile': mob,
        'tablet': tab,
        'brand':brand,
    }
    return render(request, 'webTemp/index.html',context)




def checkout_complete(request):
    return render(request,'webTemp/checkout_complete.html')



## create checkout All info view function
def checkout_info(request):
    current_user=request.user
    if request.method=="POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('Lastname')
        country = request.POST.get('Country')
        area_code = request.POST.get('AreaCode')
        primary_phone = request.POST.get('PrimaryPhone')
        address1 = request.POST.get('address1')
        zipcode = request.POST.get('Zipcode')
        print(first_name,last_name,country,area_code,primary_phone,address1,zipcode)
        # Create a new Customer object and save it
        customer = ShippingAddress(
            user=current_user,
            firstname=first_name,
            lastname=last_name,
            country=country,
            areacode=area_code,
            primaryphone=primary_phone,
            streetaddress=address1,
            zipcode=zipcode
        )
        customer.save()
        return redirect('/checkout_payment')

    return render(request,'webTemp/checkout_info.html')


def checkout_payment(request):
    return render(request,'webTemp/checkout_payment.html')


def faq(request):
    return render(request,'webTemp/faq.html')

def index_fixed_header(request):
    return render(request,'webTemp/index_fixed_header.html')


def index_inverse_header(request):
    return render(request,'webTemp/index_inverse_header.html')

def my_account(request):
    return render(request,'webTemp/my_account.html')


## We are create product deatil view function:
def product_detail(request,id):
    produt=Product.objects.filter(id=id).first()
    all_pro=Product.objects.all()
    
    ## we are fatch all product image in "ProductImagegallery"Model 
    proimg=ProductImagegallery.objects.filter(product_id=id)
    Addtionainfor=Addtionalinfo.objects.filter(product_id=id)
    contxt={
        'produt':produt,
        'proimg':proimg,
        'all_pro'   : all_pro,
        'Adinfo':Addtionainfor,
    }
    return render(request,'webTemp/product_detail.html',contxt)

## create product view function:
def product(request):
    mob = Product.objects.filter(category__catname ='Mobile')
    prod=Product.objects.all()
    cont={
        "prod":prod,
        'mobile':mob,
    }
    return render(request,'webTemp/product.html',cont)


## Create search keyword product views function:
def search_results(request):
    query=request.GET.get('Query')
    product=Product.objects.filter(tital__icontains=query)
    brand=Brand.objects.all()
    context={
        'pro':product,
        'query':query,
        'brand':brand,
    }
    return render(request,'webTemp/search_results.html',context)




## user register view functions:
def sign_in(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return HttpResponseRedirect('/login')
    return render(request ,'webTemp/sign_in.html')


## user login and authenticate user view function
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("Password")
        user_auth = authenticate(request, username=username , password=password)
        if user_auth is not None:
            login(request, user_auth)
            return HttpResponseRedirect('/index')  # Redirect to the home page after login
        else:
            messages.error(request, 'Invalid username or password')
        
    return render(request, 'webTemp/login.html')



# create the contact_us View function
def contact_uss(request):
    if request.method == 'POST':
        nam=request.POST.get('name')
        ema=request.POST.get('email')
        subj=request.POST.get('subject')
        mes=request.POST.get('message')
        print(nam,ema,subj,mes)
        contact=contactUs(name=nam,email=ema,subject=subj,message=mes)
        contact.save()

        return HttpResponseRedirect('/index')

    return render(request,'webTemp/contact_us.html')

## All product show in cart view function
def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart_products = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0

        for item in cart_products:
            item.total_price = item.quantity * item.product.price
            amount += item.total_price
        
        total_amount = amount + shipping_amount

        context = {
            'carts': cart_products,
            'total_amount': total_amount,
            'shipping_amount': shipping_amount,
            'amount': amount,
        }

        return render(request, 'webTemp/checkout_cart.html', context)
    ## we are pass total amount in the check out payment in the template
        return render(request,'webTemp/checkout_payment.html', context)
    else:
    
        pass

def increase_cart_quantity(request, product_id):
    if request.user.is_authenticated:
        user = request.user
        cart_item = Cart.objects.get(user=user, product_id=product_id)
        cart_item.quantity += 1
        cart_item.save()
    return redirect('show_cart')

def decrease_cart_quantity(request, product_id):
    if request.user.is_authenticated:
        user = request.user
        cart_item = Cart.objects.get(user=user, product_id=product_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
    return redirect('show_cart')

def remove_cart_item(request, product_id):
    if request.user.is_authenticated:
        user = request.user
        Cart.objects.filter(user=user, product_id=product_id).delete()
    return redirect('show_cart')



@login_required(login_url="/login")

def checkout_cart(request):
    user=request.user
    product_id=request.GET.get('produt_id')
    product=Product.objects.get(id=product_id)
    cart=Cart(user=user , product=product)
    cart.save()
 
    return redirect('/cart_item')        
    

# def orderplace(request):
#     current_user=request.user
#     cart=Cart.objects.filter(user=current_user)
#     for c in cart:
#         order=orderplace(user=current_user,product=c.product,Quantity=c.quantity)
#         order.save()
#         c.delete()
#         return redirect('checkout_complete')




def footer(request):
    return render(request,'webTemp/footer.html')

def about_us(request):
    return render(request,'webTemp/about_us.html')

# def checkout_cart(request):
#     return render(request,'webTemp/checkout_cart.html')