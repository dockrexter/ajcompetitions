from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views import generic
from home.models import *
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import user_passes_test
# from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
import random





# Create your views here.

# def admin_login(request):
#     return render(request,"admin/admin_index.html", {'Competition':Competiton,'total_competitions':total_competitions})

def admin(request):
    print(request.user,"apple")
    if request.user.is_superuser:
        Competiton = competition.objects.all()
        total_competitions=competition.objects.all().count()
        return render(request,"adminPanel/admin_index.html", {'Competition':Competiton,'total_competitions':total_competitions})
    else:
        return HttpResponseRedirect("/login")

def logout(request):
    try:
        del request.session['member_id']
        auth_logout(request)
    except KeyError:
        pass
    return HttpResponseRedirect("/login")
# @user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    if request.user.is_superuser:
        Competiton = competition.objects.all()
        total_competitions=competition.objects.all().count()
        return render(request,"adminPanel/admin_index.html", {'Competition':Competiton,'total_competitions':total_competitions})
    else:
        return HttpResponseRedirect("/login")

    
# @user_passes_test(lambda u: u.is_superuser)
def createCompetition(request):
    if request.user.is_superuser:
        return render(request,"adminPanel/create_competition.html")
    else:
        pass
    # return HttpResponse(request.user)
    #Competitions = competition.objects.all()
    #form=CompetitionForm1()
    #context={'Competitions':Competitions,'form':form}
        
    
# @user_passes_test(lambda u: u.is_superuser)
def saveCompetition(request): 
    # and request.FILES['image1'] and request.Files['image2']
    if request.method == "POST" and request.FILES['image'] :
        image=request.FILES['image']
        image1=request.FILES['image1']
        image2=request.FILES['image2']
        fs=FileSystemStorage()
        filename=fs.save(image.name,image)
        filename1=fs.save(image1.name,image1)
        filename2=fs.save(image1.name,image2)
        uploaded_file_url=filename
        uploaded_file_url1=filename1
        uploaded_file_url2=filename2
        print(uploaded_file_url)
        name=request.POST.get('name',None)
        desc=request.POST.get('description',None)
        det=request.POST.get('detail',None)
        question=request.POST.get('question1',None)
        nooftickets=request.POST.get('no_of_tickets',None)
        ticket_price=request.POST.get('ticket_price',None)
        time=request.POST.get('end_time',None)
        # img=request.POST.get('image',None)
        #                img=request.POST.get('image',None)

        competition_obj = competition(name=name,description=desc,no_of_tickets=nooftickets,image=uploaded_file_url,image1=uploaded_file_url1,image2=uploaded_file_url2,price=ticket_price,end_time=time,status=0,detail=det,question1=question)
        competition_obj.save()
        Competitions=competition.objects.all()
    return render(request, 'adminPanel/show_competition.html',{'Competitions':Competitions})




# @user_passes_test(lambda u: u.is_superuser)
def showCompetition(request): 
    Competitions = competition.objects.all()  
    return render(request,"adminPanel/show_competition.html",{'Competitions':Competitions})

def showUsers(request):
    users = User.objects.all()  
    return render(request,"adminPanel/show_users.html",{'Users':users})

def showTickets(request): 
    ticket = tickets.objects.all()  
    return render(request,"adminPanel/show_tickets.html",{'tickets':ticket})

def winners(request): 
    winners = winner.objects.all()  
    return render(request,"adminPanel/show_winners.html",{'winners':winners})

def draw(request):
    competition.objects.filter(name=request.GET.get("comp",None)).update(status=1)
    comp=tickets.objects.filter(competition_id=competition.objects.filter(name=request.GET.get("comp",None))[0]).values_list('id', flat=True)
    winner_obj = winner(ticket=tickets.objects.filter(id=random.choice(comp))[0])
    winner_obj.save()
    return HttpResponse(comp)

# @user_passes_test(lambda u: u.is_superuser)
def editCompetition(request,id):  
    edit_competition = competition.objects.get(id=id)
    return render(request,"adminPanel/edit_competition.html",{'edit_competition':edit_competition})


def editUser(request,id):  
    
    try:
        user = User.objects.get(id=id)
        profile=Profile.objects.get(user=user)
        return render(request,"adminPanel/edit_user.html",{'User':user,'Profile':profile})
    except:
        user = User.objects.get(id=id)
        return render(request,"adminPanel/edit_user.html",{'User':user})

def addUsers(request):
    return render(request,"adminPanel/add_user.html")


def saveUsers(request):
    user_name = request.POST.get('username', None)
    user_pass = request.POST.get('password', None)
    user_mail = request.POST.get('email', None)
    user = User.objects.create_user(username=user_name,email=user_mail,password=user_pass)
    is_staff=request.POST.get('is_staff',None)
    is_superuser=request.POST.get('is_superuser',None)
    user.is_staff=is_staff
    user.is_superuser=is_superuser
    user.save()
    return HttpResponseRedirect('/admin/showusers')
    

# @user_passes_test(lambda u: u.is_superuser)
def updateCompetition(request,id):
    if request.method == "POST" and request.FILES:
        image=request.FILES['image']
        fs=FileSystemStorage()
        filename=fs.save(image.name,image)
        uploaded_file_url=filename
        update_competition=competition.objects.get(id=id)
        comp_id=update_competition.id
        name=request.POST.get('name',None)
        desc=request.POST.get('description',None)
        nooftickets=request.POST.get('no_of_tickets',None)
        ticket_price=request.POST.get('ticket_price',None)
        question=request.POST.get('question1',None)
        det=request.POST.get('detail',None)
        time=request.POST.get('end_time',None)
        print(time)
        competition.objects.filter(pk=comp_id).update(name=name,description=desc,no_of_tickets=nooftickets,image=uploaded_file_url,price=ticket_price,end_time=time,detail=det,question1=question)
        Competitions=competition.objects.all()
        return render(request, 'adminPanel/show_competition.html',{'Competitions':Competitions})
    else:
        update_competition=competition.objects.get(id=id)
        comp_id=update_competition.id
        uploaded_file_url=update_competition.image
        name=request.POST.get('name',None)
        desc=request.POST.get('description',None)
        ticket_price=request.POST.get('ticket_price',None)
        question=request.POST.get('question1',None)
        nooftickets=request.POST.get('no_of_tickets',None)
        det=request.POST.get('detail',None)
        time=request.POST.get('end_time',None)
        print(time,"apple")
        competition.objects.filter(pk=comp_id).update(name=name,description=desc,no_of_tickets=nooftickets,image=uploaded_file_url,price=ticket_price,end_time=time,detail=det,question1=question)
        Competitions=competition.objects.all()
        return render(request, 'adminPanel/show_competition.html',{'Competitions':Competitions})

def updateUser(request,id):
    is_staff=request.POST.get('is_staff',None)
    is_superuser=request.POST.get('is_superuser',None)
    User.objects.filter(pk=id).update(is_superuser=is_superuser,is_staff=is_staff)
    return HttpResponseRedirect('/admin/editUser/'+str(id))
def deleteCompetition(request,id):
    update_competition=competition.objects.filter(id=id).delete()
    return HttpResponseRedirect('/admin')