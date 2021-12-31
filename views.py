from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import connection

from pages.models import SitePassword

# Create your views here.
def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username != "" and password != "":
            User.objects.create_user(username=username, password=password)
            return redirect('/login/')

    return redirect('/')

@login_required
def addPassword(request):
    if request.method == 'POST':
        site = request.POST.get('site')
        password = request.POST.get('sitePassword')

        if site != "" and password != "":
            SitePassword.objects.create(user=request.user, site=site, password=password)

    return redirect('/')

def getPasswords(request, id=-1):
    if id != -1:
        myPasswords = SitePassword.objects.filter(user=User.objects.get(id=id))
        return render(request, 'passwords.html', {'myPasswords': myPasswords})

    return redirect('/')

@login_required
def filter(request, id=-1):
    if request.method == 'POST':
        filter = request.POST.get('filter')

        if filter != "" and id != -1:
            username = User.objects.get(id=id).username
            passwords = SitePassword.objects.raw("SELECT id, user, site, password FROM SitePassword WHERE site='%s'" % (filter))

            list = []
            for item in passwords:
                if str(item.user) == username:
                    list.append({'site': item.site, 'password': item.password})

            return render(request, 'passwords.html', {'myPasswords': list})

    return redirect('/passwords/{0}/'.format(id))
