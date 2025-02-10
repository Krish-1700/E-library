from django.shortcuts import render
from django.db.models import Q
from shop.models import Products

def search(request):
    if (request.method == "POST"):
        q =request.POST.get('q')
        s = Products.objects.filter(Q(name__icontains=q) | Q(desc__icontains=q))
        context = {'find': s}
    return render(request, 'search.html', context)
