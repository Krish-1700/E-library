from lib2to3.fixes.fix_input import context

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect



def home(request):
 return render(request,'home.html')



@login_required
def viewbook(request):
    b=Book.objects.all()
    context={'book':b}
    return render(request,'view.html',context)

from books.models import Book
@login_required
def addbook(request):
    if(request.method=="POST"):
     tit =request.POST['t']
     auth = request.POST['a']
     pri = request.POST['p']
     pag = request.POST['pg']
     lan = request.POST['l']
     img = request.FILES['i']
     pdf = request.FILES['f']
     b =Book.objects.create(title=tit, author=auth, price=pri, pages=pag, language=lan, image=img, pdf=pdf)
     b.save()
     return redirect('books:home')





    return render(request,'add.html')

@login_required
def factorial(request):
    if(request.method=="POST"):
        num=int(request.POST['n'])
        print(num)

        f=1
        for i in range(1,num+1):
            f=f*i
        return render(request, 'fact.html',{'fact':f})
    return render(request,'fact.html')

@login_required
def details(request,i):
    b=Book.objects.get(id=i)
    context={'book':b}
    return render(request,'details.html',context)
@login_required
def deletebook(request,i):
    b=Book.objects.get(id=i)
    b.delete()
    return redirect('books:viewbook')
@login_required
def editbook(request,i):
    b=Book.objects.get(id=i)
    if (request.method == "POST"):
        b. title=request.POST['t']
        b.author=request.POST['a']
        b.price=request.POST['p']
        b.pages=request.POST['pg']
        b.language=request.POST['l']
        if(request.FILES.get('i')==None):
            b.save()
        else:
            b.image=request.FILES.get('i')
            b.save()
        if(request.FILES.get('f')==None):
            b.save()
        else:
           b.pdf =request.FILES.get('f')
        b.save()
        return redirect('books:viewbook')

    context={'book':b}
    return render(request,'edit.html',context)

from django.db.models import Q
@login_required
def search(request):
    if(request.method=="POST"):
        query=request.POST['q']
        b=Book.objects.filter(Q(title__icontains=query)|Q(author__icontains=query))
        context={'book':b}
    return render(request,'search.html',context)