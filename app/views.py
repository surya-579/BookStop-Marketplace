from django.http.response import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *
from .forms import *
from logging import exception
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class ProductView(View):
				def get(self, request):

					Medical = Product.objects.filter(category='Me')
					

					Mechanical = Product.objects.filter(category='Mec')
			

					Engineering = Product.objects.filter(category='Eng')
	

					return render(request, 'app/home.html', {'Medical': Medical, 'Mechanical': Mechanical, 'Engineering': Engineering})


class ProductDetailView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        
        # Fetch customer details
        customer = get_object_or_404(Customer, user=product.user)
        
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(
                Q(product=product.id) & Q(user=request.user)).exists()

        context = {
            'product': product,
            'customer': customer,
            'item_already_in_cart': item_already_in_cart,
        }
        return render(request, 'app/productdetail.html', context)


@login_required
def add_to_cart(request):
 user = request.user
 product_id = request.GET.get('prod.id')
 size_id = request.GET.get('size.id')
 if size_id == None:
  size_id = "watch"
 print(size_id)
 product = Product.objects.get(id=product_id)
 Cart(user=user, product=product, Size=size_id).save()
 return redirect('/cart/')


@login_required
def show_cart(request):
  if request.user.is_authenticated:
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 70.0
    total_amount = 0.0
    cart_product = [p for p in Cart.objects.all() if p.user == user]
    
    if cart_product:
         for p in cart_product:
           tempamount = (p.quantity * p.product.discount_price)
           amount += tempamount
           totalamount = amount+shipping_amount
         return render(request, 'app/addtocart.html', {'carts': cart, 'totalamount': totalamount, 'amount': amount})
    else:
      return render(request, 'app/emptycart.html')


@login_required
def plus_cart(request):
  if request.method == 'GET':
        prod_id = request.GET['prod_id']
        user = request.user
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0

        cart_product = [p for p in Cart.objects.all() if p.user == user]
        for p in cart_product:
               tempamount = (p.quantity * p.product.discount_price)
               amount += tempamount
               totalamount = amount+shipping_amount
        data = {
                 'quantity': c.quantity,
                 'amount': amount,
                 'totalamount': totalamount
                              }
        return JsonResponse(data)


@login_required
def minus_cart(request):
      if request.method == 'GET':
        prod_id = request.GET['prod_id']
        user = request.user
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        if c.quantity != 1:
          
          c.quantity -= 1
          c.save()
          amount = 0.0
          shipping_amount = 70.0
          total_amount = 0.0
          cart_product = [p for p in Cart.objects.all() if p.user == user]
          for p in cart_product:
               tempamount = (p.quantity * p.product.discount_price)
               amount += tempamount
               totalamount = amount+shipping_amount
          data = {
                 'quantity': c.quantity,
                 'amount': amount,
                 'totalamount': totalamount
                              }
        return JsonResponse(data)


@login_required
def remove_cart(request):
      if request.method == 'GET':
        prod_id = request.GET['prod_id']
        user = request.user
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        totalamount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        for p in cart_product:
               tempamount = (p.quantity * p.product.discount_price)
               amount += tempamount
               totalamount = amount+shipping_amount
        data = {

                 'amount': amount,
                 'totalamount': totalamount
                              }
        return JsonResponse(data)


@login_required
def buy_now(request):
 user = request.user
 product_id = request.GET.get('prod.id')
 size_id = request.GET.get('size.id')
 product = Product.objects.get(id=product_id)


 Cart(user=user, product=product, Size=size_id).save()
 return redirect('/cart/')


@login_required
def address(request):
 add = Customer.objects.filter(user=request.user)

 return render(request, 'app/address.html', {'add': add})



def mobile(request):
 return render(request, 'app/mobile.html')


def login(request):
 return render(request, 'app/login.html')


class CustomerRegistrationView(View):
 def get(self, request):
   form = CustomerRegistrationForm()
   return render(request, 'app/customerregistration.html', {'form': form})

 def post(self, request):
     form = CustomerRegistrationForm(request.POST)
     if form.is_valid():
       messages.success(request, 'congrates registeration successfull')
       form.save()
     return render(request, 'app/customerregistration.html', {'form': form})


@login_required
def checkout(request):
      user = request.user
      add = Customer.objects.filter(user=user)

      if add:
         cart_items = Cart.objects.filter(user=user)
         amount = 0.0
         shipping_amount = 70.0
         totalamount = 0.0
         cart_product = [p for p in Cart.objects.all() if p.user == user]
         if cart_product:
               for p in cart_product:
   
                     tempamount = (p.quantity * p.product.discount_price)
        
                     amount += tempamount
               totalamount = amount+shipping_amount
               
         return render(request, 'app/checkout.html', {'add': add, 'totalamount': totalamount, 'cart_items': cart_items})
      return redirect("/profile/")


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
      form = CustomerProfileForm()
      add = Customer.objects.filter(user=request.user)

      return render(request, 'app/profile.html', {'form': form, 'add': add[0:2]})

    def post(self, request):
         form = CustomerProfileForm(request.POST)
         add = Customer.objects.filter(user=request.user)
         if form.is_valid():
           usr = request.user
           name = form.cleaned_data['name']
           rollNumber = form.cleaned_data['rollNumber']
           branch = form.cleaned_data['branch']
           phoneNumber = form.cleaned_data['phoneNumber']

           reg = Customer(user=usr, name=name, rollNumber=rollNumber,
                          branch=branch,phoneNumber=phoneNumber)
           reg.save()
           messages.success(request, 'congratulation address is added')
         return render(request, 'app/profile.html', {'form': form, 'add': add})
      








@method_decorator(login_required, name='dispatch')
class CustomerDeleteView(View):
  def get(self, request, pk):
    c = Customer.objects.get(pk=pk)
    c.delete()
    return redirect("/profile/")


def Contact(request):
  form = ContactForm(request.POST)
  if form.is_valid():
    form.save()
  return render(request,'app/contact.html',{'form':form})

  # 404 pages

def err_404(request, exception):
    err = '404'
    return render(request, 'app/404.html', {'err':err, 'msg':'Page not found'})

def err_500(request, *args,):
    err = '500'
    return render(request, 'app/404.html', {'err':err, 'msg':'There is a Server Error'})

# def handler_500_page(request, *args, **argv):
#   return render(request, 'app/404page.html')


@login_required
@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return JsonResponse({'status': 'success', 'message': 'Product added successfully'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = ProductForm()
    return render(request, 'app/manage_products.html', {'form': form})

@login_required
def list_user_products(request):
    products = Product.objects.filter(user=request.user)
    products_list = [
        {
            'id': product.id,
            'title': product.title,
            'selling_price': product.selling_price,
            'discount_price': product.discount_price,
            'description': product.description,
            'category': product.category,
        }
        for product in products
    ]
    return JsonResponse(products_list, safe=False)

@login_required
def get_product_details(request, pk):
    product = get_object_or_404(Product, pk=pk, user=request.user)
    product_data = {
        'title': product.title,
        'selling_price': product.selling_price,
        'discount_price': product.discount_price,
        'description': product.description,
        'category': product.category,
        'product_img': product.product_img.url if product.product_img else '',
        'product_imag': product.product_imag.url if product.product_imag else '',
        'product_image': product.product_image.url if product.product_image else '',
        'product_images': product.product_images.url if product.product_images else '',
    }
    return JsonResponse(product_data)

@login_required
@csrf_exempt
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Product updated successfully'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    else:
        form = ProductForm(instance=product)
    return render(request, 'app/manage_products.html', {'form': form})

@login_required
@csrf_exempt
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk, user=request.user)
    if request.method == 'POST':
        product.delete()
        return JsonResponse({'status': 'success', 'message': 'Product deleted successfully'})
    return render(request, 'app/manage_products.html', {'product': product})