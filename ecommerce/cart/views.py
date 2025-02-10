from http.client import responses
from lib2to3.fixes.fix_input import context
from locale import currency

import razorpay
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from shop.models import Products
from cart.models import Cart

from cart.models import Payment, Order_details


@login_required
def addtocart(request,i):
    u=request.user            #get the details of current user
    p=Products.objects.get(id=i)  #get the all details of particular products
    try:
        cart=Cart.objects.get(user=u,product=p)  #for increment
        if(p.stock>0):
            cart.quantity +=1
            cart.save()
            p.stock -=1
            p.save()
    except:
        if(p.stock):
            cart=Cart.objects.create(user=u, product=p, quantity=1)
            cart.save()
            p.stock -=1
            p.save()
    return redirect('cart:cartview')

@login_required
def cartview(request):
    u=request.user
    c=Cart.objects.filter(user=u)
    total=0
    for i in c:
        total+=i.product.price*i.quantity

    context={'cart':c,'total':total}
    return render(request,'cart.html',context)


def cart_decrement(request,pk):               #for decrement
    p=Products.objects.get(id=pk)
    u=request.user
    try:
        cart=Cart.objects.get(user=u,product=p)
        if(cart.quantity>1):
            cart.quantity -=1
            cart.save()
            p.stock +=1
            p.save()

        else:
            cart.delete()
            p.stock +=1
            p.save()

    except:
        pass
    return redirect('cart:cartview')


def cart_delete(request,i):
    u=request.user
    p=Products.objects.get(id=i)
    try:
        cart=Cart.objects.get(user=u,product=p)
        cart.delete()
        p.stock += cart.quantity
        p.save()

    except:
        pass
    return redirect('cart:cartview')


def order_form(request):
    if (request.method == 'POST'):
        a = request.POST['a']
        pin = request.POST.get('pin')
        ph = request.POST['ph']
        print(pin)
        u=request.user
        c=Cart.objects.filter(user=u)
        total=0
        for i in c:
            total+=i.quantity*i.product.price
        total=int(total)

        #Razorpay client connection
        client=razorpay.Client(auth=('rzp_test_cAPhHxa4cHFPHh','CXEHuwvRpjeP5rcSIcsMcc6C'))

        #Razorpay order creation
        response_payment=client.order.create(dict(amount=total*100,currency='INR'))
        print(response_payment)

        order_id=response_payment['id']
        status=response_payment['status']

        if(status=='created'):
            p=Payment.objects.create(name=u.username,amount=total,order_id=order_id)
            p.save()


            for i in c:
                o=Order_details.objects.create(product=i.product,user=i.user,phone=ph,pin=pin,address=a,order_id=order_id,no_of_items=i.quantity)
                o.save()

            context={'payment':response_payment,'name':u.username}
            return render(request,'payment.html',context)


    return render(request,'order.html')

from django.contrib.auth.models import User
@csrf_exempt
def status(request,p):
    user=User.objects.get(username=p)
    login(request,user)

    response=request.POST
    print(response)

    param_dict={
        'razorpay_order_id':response['razorpay_order_id'],
        'razorpay_payment_id':response['razorpay_payment_id'],
        'razorpay_signature':response['razorpay_signature']
    }
    client=razorpay.Client(auth=('rzp_test_cAPhHxa4cHFPHh','CXEHuwvRpjeP5rcSIcsMcc6C'))
    try:
        status=client.utility.verify_payment_signature(param_dict)
        print(status)
        p=Payment.objects.get(order_id=response['razorpay_order_id'])
        p.paid=True
        p.razorpay_payment_id=response['razorpay_payment_id']
        p.save()

        o = Order_details.objects.filter(order_id=response['razorpay_order_id'])
        for i in o:
            i.payment_status = "completed"
            i.save()
        c=Cart.objects.filter(user=user)
        c.delete()
    except:
        pass



    return render(request,'status.html')

def order_view(request):
    u=request.user
    o=Order_details.objects.filter(user=u,payment_status="completed")
    context={'orders':o}
    return render(request,'order_view.html',context)

