from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from store.models import Product,Cart,Wishlist
from django.contrib.auth.decorators import login_required

@login_required(login_url='loginpage')
def index(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context ={'wishlist':wishlist}
    return render(request,'store/wishlist.html',context)

def addtowishlist(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if(Wishlist.objects.filter(user=request.user.id,product_id=prod_id)):
                    return JsonResponse({'status': "Product is already  in list"})
                else:
                    Wishlist.objects.create(user=request.user , product_id = prod_id)
                    return JsonResponse({'status':"Product add to wishlist succesfully"})
            else:
                return JsonResponse({'status':"No such product found"})
        else:
            return JsonResponse({'status': "Login to continue"})
    return redirect('/')
                
              
