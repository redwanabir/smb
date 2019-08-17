from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .models import Merchandiser
from .models import reg

def index(request):
    return render(request, 'homepage/index.html')


def about(request):
    return render(request, 'about.html')


def list(request):
    user = Merchandiser.objects.all()
    return render(request, 'reg_merchandiser.html',
                  {'users': user})

def login(request):
    l = reg(phone_no=request.POST.get('phone_no'), password=request.POST.get('password'))
    l.save()
    return render(request, 'login.html')


def addMerchandiser(request):  # adding new user
    user = Merchandiser(name=request.POST.get('name'), store=request.POST.get('store'), address=request.POST.get('address'),
                            zip_code=request.POST.get('zip_code'), phone_no=request.POST.get('phone_no'),
                            tin_no=request.POST.get('tin_no'), date_of_birth=request.POST.get('date_of_birth'),
                            optional_website=request.POST.get('optional_website'), password=request.POST.get('password'),
                            c_password=request.POST.get('c_password'))

    user.save()
    #return HttpResponseRedirect('/addMerchandiser/')
    return render(request, 'reg_merchandiser.html')
