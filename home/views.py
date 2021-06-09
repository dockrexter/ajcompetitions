'''
@Developers 
Muhammad Shaheer Rahi
Huzaifa Ahmed

@Company: Texus 

'''
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import generic
from .models import *
from django.contrib.auth.decorators import user_passes_test
from cart.cart import Cart
from django.shortcuts import redirect
from datetime import datetime

# Current date time in local system


# Create your views here.

class PostDetail(generic.DetailView):
    model=competition
    template_name='home/post_detail.html'


def index(request):
    
    competitions = competition.objects.all()
    if request.session._session:
        context={
            "user":User.objects.filter(id=request.session['member_id']).values('username')[0]['username'],
            "competitions":competitions
        }
        print(context)
    else:
        context={
            "user":None,
            "competitions":competitions
        }
        print(context)

    return render(request, 'home/index.html',context)



def logout(request):
    try:
        del request.session['member_id']
        auth_logout(request)
    except KeyError:
        pass
    return render(request,'home/login.html')



def login(request):

    if request.method == 'POST':
        user_name = request.POST.get('username', None)
        user_pass = request.POST.get('password', None)
        print(user_name,user_pass)
        user = authenticate(username=user_name, password=user_pass)
        print(user)
        
        
        if user is not None:
            # A backend authenticated the credentials
            request.session['member_id'] = user.id
            auth_login(request,user)
            if user.is_superuser:
                print(user)
                return HttpResponseRedirect("/admin/dashboard")
            return index(request)
        else:
            # No backend authenticated the credentials
            return render(request, 'home/login.html')
    else:
        if request.user.is_authenticated:
            return render(request, 'home/login.html',{"User":request.user})
        else:
            return render(request, 'home/login.html')

    

def register(request):
    if request.method == 'POST':
        user_name = request.POST.get('email', None)
        user_pass = request.POST.get('password', None)
        user_mail = request.POST.get('email', None)
        user_fname = request.POST.get('firstname', None)
        user_lname = request.POST.get('lastname', None)
        user_ph = request.POST.get('telephone', None)
        data={
            "username":user_name,
            "password":user_pass,
            "email":user_mail,
            "firstname":user_fname,
            "lastname": user_lname,
            "phonenumber":user_ph
        }
        try:
            user = User.objects.create_user(username=user_name,email=user_mail,first_name=user_fname,last_name=user_lname,password=user_pass)
            user.is_staff = False
            user.is_superuser=False
            user.save()
            pro=Profile(user=user,phonenumber=user_ph)
            pro.save()
            return HttpResponseRedirect('/login')
        except:
            return render(request, 'home/register.html',{'Message':"username already exist","user":data})

        

    return render(request, 'home/register.html')



def draws(request):
    competitions = competition.objects.all()
    if request.session._session:
        context={
            "user":User.objects.filter(id=request.session['member_id']).values('username')[0]['username'],
            "competitions":competitions
        }
        print(context)
    else:
        context={
            "user":None,
            "competitions":competitions
        }
        print(context)
    return render(request, 'home/draws.html',context)

def winners(request):
    winners=winner.objects.all()
    context={
        "winners":winners
    }
    return render(request,'home/winners.html',context)

def how_to(request):
    return render(request,'home/howto.html')





def competitions(request):
    competitions = competition.objects.all()
    if request.session._session:
        context={
            "user":User.objects.filter(id=request.session['member_id']).values('username')[0]['username'],
            "competitions":competitions
        }
        print(context)
    else:
        context={
            "user":None,
            "competitions":competitions
        }
        print(context)
    return render(request, 'home/draws.html',context)


def ticket(request):
    items=request.session.get('cart')
    for key, value in items.items():
        for i in range(0,value["quantity"]):
            # ticket_inst=tickets(competition_id=competition.objects.get(id=value["product_id"]),user_id=User.objects.get(id=value["userid"]))
            # ticket_inst.save()
            no=competition.objects.filter(id=value["product_id"]).values("sold_tickets")
            print(no[0]["sold_tickets"]+1)
            comp=competition.objects.filter(id=value["product_id"]).update(sold_tickets=no[0]["sold_tickets"]+1)
            print(comp)
            comp.save()
    cart_clear()
    return HttpResponse("Success!")


 #cart views
@login_required(login_url="/login")
def cart_add(request, id):
    cart = Cart(request)
    product = competition.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_clear(request, id):
    cart = Cart(request)
    product = competition.objects.get(id=id)
    cart.remove(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_increment(request, id):
    cart = Cart(request)
    product = competition.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = competition.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_detail(request):
    promo = promos.objects.all()
    return render(request, 'home/cart_detail.html',{'Promos':promo})