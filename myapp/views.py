from django.shortcuts import render
from .models import Category,Game,Turnir,Comentary,Contact,Forum,Adress1,Profil
from django.db.models import Q
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.core.paginator import Paginator
from .forms import Profil1,TurnirQoshish,TurnirUpdateForm,ProfilUpdateForm,ContactUpdate
from accounts.models import CustomUser
from django.contrib import messages
import os
from django.core.paginator import Paginator




# Create your views here.

def index(request):

    games = Game.objects.order_by('-comentNum')[:4]
    games2 = Game.objects.order_by('-views')[:3].all()
    categories = Category.objects.all()
    games1 = Game.objects.order_by('-like')[:3]
    turnirlar = Turnir.objects.all()
    reviews = Game.objects.order_by('-date')[:4]
    comments = Comentary.objects.order_by('-commentNum')[:4]
    users = CustomUser.objects.all()
    

    # count = Game.objects.count()
    

    if request.method == 'POST' and request.POST.get('id') :
        print(request.POST)
        
        ball = request.POST['ball']
        bal1 = Game.objects.get(id=request.POST.get('id'))
        bal1.ball = ball
        bal1.save()

    elif request.method == 'GET' and request.GET.get('like') == 'like' and request.GET.get('id'):
        gameid = request.GET.get('id')

        gameObj = Game.objects.get(id=int(gameid))
        gameObj.like = gameObj.like + 1
        gameObj.save()

    


    context = {
        "user": request.user,
        "games":games,
        "categories":categories,
        "games1":games1,
        "turnirlar":turnirlar,
        "reviews":reviews,
        "comments":comments,
        "games2":games2,
        "users":users,
        # "count":count,
    }

    return render(request=request,template_name='blog/index.html',context=context)

def categories(request):
    categories = Category.objects.all()
    comments = Comentary.objects.order_by('-commentNum')[:4]
    likes = Game.objects.all()
    games1 = Game.objects.order_by('-like')[:2]
    posts = Profil.objects.all()


    pages = Paginator(likes,6)
    page_number1 = request.GET.get('page') 
    page_obj = pages.get_page(page_number1)
    



    if 'query' in request.GET:
        query = request.GET['query']
        games3 = Game.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))

    elif request.method == 'GET' and request.GET.get('like') == 'like' and request.GET.get('id'):
        gameid = request.GET.get('id')

        gameObj = Game.objects.get(id=int(gameid))
        gameObj.like = gameObj.like + 1
        gameObj.save()
        likes = Game.objects.all()

    else:
        games3 = Game.objects.order_by('-id')


    
  

    
    context = {
        "page_obj":page_obj,
        "categories":categories,
        "comments":comments,
        "games1":games1,
        "posts":posts,


    }
    return render(request=request,template_name='blog/categories.html',context=context)

def community(request):
    comments = Comentary.objects.order_by('-commentNum')[:4]
    categories = Category.objects.all()
    comments1 = Forum.objects.all()
    games1 = Game.objects.order_by('-like')[:3]
    comment = Forum.objects.all()
    posts = Profil.objects.all()
    

    pages = Paginator(comments1,6)
    page_number = request.GET.get('page')
    page_obj = pages.get_page(page_number)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        body = request.POST['body']

        body1 = Forum(name=name,email=email,subject=subject,body=body)
        body1.save()
        

    context = {
        "page_obj":page_obj,
        "categories":categories,
        "comments":comments,
        "games1":games1,
        "comment":comment,
        "posts":posts,
    }
    return render(request=request,template_name='blog/community.html',context=context)

def contact(request):
    categories = Category.objects.all()
    games1 = Game.objects.order_by('-like')[:3]
    comments = Comentary.objects.order_by('-commentNum')[:4]
    posts = Profil.objects.all()
    if request.method == 'POST' and request.POST.get('message'):
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        massage = request.POST['message']
        message1 = Contact(name=name,email=email,subject=subject,massage=massage)
        message1.save()
    context = {
        "categories":categories,
        "comments":comments,
        "games1":games1,
        "posts":posts,

        
    }
    return render(request=request,template_name='blog/contact.html',context=context)

def review(request):
    comments = Comentary.objects.order_by('-commentNum')[:4]
    reviews = Game.objects.order_by('-ball')[:4]
    sharh = Game.objects.order_by('-date')[:4]
    categories = Category.objects.all()
    games1 = Game.objects.order_by('-like')[:3]
    posts = Profil.objects.all()


    context = {
        "reviews":reviews,
        "sharh":sharh,
        "categories":categories,
        "comments":comments,
        "games1":games1,
        "posts":posts,
    }
    return render(request=request,template_name='blog/review.html',context=context)

def singleBlog(request,id):
    post = Game.objects.get(id=id)
    categories = Category.objects.all()
    games1 = Game.objects.order_by('-like')[:3]
    comments = Comentary.objects.order_by('-commentNum')[:4]
    posts = Profil.objects.all()

    # if request.method == 'GET' and request.GET.get('id'):

    

    context = {
        "categories":categories,
        "comments":comments,
        "games1":games1,
        "post":post,
        "posts":posts,

    }
    return render(request=request,template_name='blog/singleBlog.html',context=context)

def search(request):
    comments = Comentary.objects.order_by('-commentNum')[:4]
    games1 = Game.objects.order_by('-like')[:3]
    categories = Category.objects.all()
    posts = Profil.objects.all()

    if request.GET:
        query = request.GET['query']
        games3 = Game.objects.filter(Q(oyinNomi__icontains=query) | Q(body__icontains=query))

    elif request.method == 'GET' and request.GET.get('like') == 'like' and request.GET.get('id'):
        gameid = request.GET.get('id')

        gameObj = Game.objects.get(id=int(gameid))
        gameObj.like = gameObj.like + 1
        gameObj.save()
        

        

    
    else:
        games3 = Game.objects.order_by('-id')

    pages = Paginator(games3,4)
    page_number = request.GET.get('page')
    page_obj = pages.get_page(page_number)

    context = {
        "games3":games3,
        "page_obj":page_obj,
        "comments":comments,
        "games1":games1,
        "categories":categories,
        "posts":posts,

    }

    return render(request=request,template_name='blog/search.html',context=context)


def category(request,id):

    
   
    categories = Category.objects.all()
    comments = Comentary.objects.order_by('-commentNum')[:4]
    games1 = Game.objects.order_by('-like')[:3]
    posts = Profil.objects.all()
    if request.method == 'GET' and request.GET.get('like') == 'like' and request.GET.get('id'):
        gameid = request.GET.get('id')

        gameObj = Game.objects.get(id=int(gameid))
        gameObj.like = gameObj.like + 1
        gameObj.save()
    

    post = Game.objects.get(id=id)

    context = {
        "post":post,
        "comments":comments,
        "games1":games1,
        "categories":categories,
        "posts":posts,

    }

    return render(request=request,template_name='blog/category.html',context=context)


def turnirlar(request,id):
    post = Turnir.objects.get(id=id)
    posts = Profil.objects.all()

    context = {
        "post":post,
        "posts":posts,
        

    }

    return render(request=request,template_name='blog/turnirlar.html',context=context)



def rasm(request):
    
    form = Profil1()
    if request.method == "POST":
        form = Profil1(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        "form":form,
        
    }
    return render (request=request,template_name='rasm.html',context=context)



def turnirqoshish(request):
    form = TurnirQoshish()
    if request.method == 'POST':
        form = TurnirQoshish(request.POST or None, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sozlamalar')
    context = {
        "form":form
    }
    return render(request=request,template_name='turnirqoshish.html',context=context)


def turnirupdate(request,id):
    
    obj = Turnir.objects.get(id=id)
    form = TurnirUpdateForm(request.POST,request.FILES, instance=obj)
    
    if form.is_valid():
        image_path = obj.image.path
        if os.path.exists(image_path):
            os.remove(image_path)
        print(form.cleaned_data['image'])
        form.save()
        return redirect('sozlamalar')
        
    

    context = {
        "form":form,
    }
    return render(request=request,template_name='turnirupdate.html',context=context)



def turnirupdate1(request):
    turnirs = Turnir.objects.all()

    context={
        "turnirs":turnirs,
    }

    return render(request,'turnirupdate1.html',context)

def turnirdelet1(request):
    turnirs = Turnir.objects.all()
   

    context={
        "turnirs":turnirs,
    }

    return render(request,'turnirdelet1.html',context)



def turnirdelet(request,id):
    obj = get_object_or_404(Turnir,id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('sozlamalar')
    context = {
        
    }
    return render(request,'turnirdelet.html',context)




def profil(request,id):
    
    if request.method == 'GET' :
        post = Profil.objects.get(id=id)
    else:
        post=None
    contacts = Contact.objects.all()
    


    
    
    context = {
    
        "post":post,
        "contacts":contacts,
        
    }
        
    return render(request=request,template_name='profil.html',context=context)



def profilupdate(request,id):
    user = CustomUser.objects.get(id=id)
    Profil.objects.get_or_create(user_id=request.user.id)
    ProfilUpdateForm()
    if request.method == 'POST':
        form = ProfilUpdateForm(request.POST or None,request.FILES,instance=request.user.profil)
        if form.is_valid():
            form.save()
            messages.success(request,f"Account Update Successfully!")
            return redirect('sozlamalar')
    else:
        form = ProfilUpdateForm(request.POST,request.FILES,instance=request.user.profil)
    context = {
        "form":form,
    }

    return render(request,'profilupdate.html',context)

def profildelet(request,id):
    obj = get_object_or_404(Profil,user_id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('index')
    return render(request,'profildelet.html')

def sozlamalar(request):
    turnirs = Turnir.objects.all()
    context={
        "turnirs":turnirs,
    }
    return render(request=request,template_name='sozlamalar.html',context=context)


def table(request,id):
    custom = Profil.objects.get(id=id)
    customData = Profil.objects.all()
    context = {
        "custom":custom,
        "customData":customData,

    }
    return render(request,'table.html',context)

def admin1(request):
    users = Profil.objects.all()
    context = {
        "users":users,
    }
    return render(request,'admin.html',context)



def sms(request):
 

    if request.method == 'POST':
        
        email = request.POST['email']
        massage = request.POST['massage']
        subject = request.POST['subject']
        natija = Contact(profile_id_id=request.user.id,email=email,massage=massage,subject=subject)
        natija.save()
        return redirect('index')
    
    return render(request,'sms.html')

def contactupdate(request,id):
    obj = Contact.objects.get(id=id)
    form = ContactUpdate(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        "form":form,
    }
    return render(request,'contactupdate.html',context=context)

def contactdelet(requset,id):
    obj = get_object_or_404(Contact, id = id)
    if requset.method == 'POST':
        obj.delete()
        return redirect('index')
    return render(request=requset,template_name='contactdelet.html')






