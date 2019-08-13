from django.shortcuts import render

# Create your views here.
from.models import Post1

def index(request):
    return render(request,'profil/index.html')

def sejarah(request):
    posts = Post1.objects.all()
    context = {
        'judul1' : 'Sejarah TK INKA',
        'h1': 'LALALALA',
        'Posts' : posts,
    }
    return render(request, 'profil/sejarah.html', context)

def vm(request):
    posts = Post1.objects.all()
    context = {
        'Posts' : posts,
    }
    return render(request, 'profil/vm.html', context)

def prestasi(request):
    return render(request, 'profil/prestasi.html')

def fasil(request):
    return render(request, 'profil/fasil.html')
