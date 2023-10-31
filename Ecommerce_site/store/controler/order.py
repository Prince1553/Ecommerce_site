from django.shortcuts import render,redirect,HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.models import User
from store.models import Product,Cart,Wishlist ,Order,OrderItem,Profile
from django.contrib.auth.decorators import login_required
import random


def index(request):
    orders = Order.objects.filter(user=request.user)
    context ={'orders':orders}
    return render(request,'store/orderitem.html',context)


def vieworder(request,t_no):
    order = Order.objects.filter(tracking_no=t_no, user=request.user).first()
    orderitems=OrderItem.objects.filter(order=order)
    context = {'order':order,'orderitems':orderitems}
    return render(request,'store/orderviews.html',context)