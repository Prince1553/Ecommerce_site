from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .forms import CustomUserform
from django.http.response import JsonResponse

# Create your views here.
def home(request):
    trending_products= Product.objects.filter(trending=1)
    category = Category.objects.filter(status=0)
    context ={'trending_products':trending_products,'category':category}
    return render(request,'store/index.html',context)

def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category':category}
    return render(request,'store/collections.html',context)

def collectionsview(request,slag):
    if(Category.objects.filter(slag=slag,status=0)):
        product=Product.objects.filter(Category__slag=slag)
        category_name=Category.objects.filter(slag=slag).first()
        context={'product':product,'category_name':category_name}
        return render(request, 'store/product/index.html',context)
    else:
        messages.warning(request,"No such category is found ")
        return redirect('collections')
    

def productview(request,cate_slag,prod_slag):
    if(Category.objects.filter(slag=cate_slag,status=0)):
        if(Product.objects.filter(slag=prod_slag,status=0)):
            products=Product.objects.filter(slag=prod_slag,status=0).first()
            context ={'products':products}

        else:
            messages.warning(request,"No such category is found ")
            return redirect('collections')


    else:
        messages.warning(request,"No such category is found ")
        return redirect('collections')
    return render(request,'store/productview.html',context)  

 
def productlistAjex(request):
    products= Product.objects.filter(status=0).values_list('name',flat=True)
    productlist = list(products)

    return JsonResponse(productlist,safe=False)


def searchproduct(request):
    if request.method == 'POST':
      searcheditem= request.POST.get('productsearch')
      if searcheditem == "":
          return redirect(request.META.get('HTTP_REFERER'))
      else:
          product = Product.objects.filter(name__contains=searcheditem).first()

          if product:
              return redirect('collections/'+product.Category.slag+'/'+product.slag)
          else:
              messages.info(request,"No product matched your search")
              return redirect(request.META.get('HTTP_REFERER'))
          
    return redirect(request.META.get('HTTP_REFERER'))    