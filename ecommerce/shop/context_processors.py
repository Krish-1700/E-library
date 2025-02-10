from .models import Category

def links(request):  #for displaying dropdown items
    c=Category.objects.all()
    return {'links':c}