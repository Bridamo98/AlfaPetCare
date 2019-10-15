from django.shortcuts import render, redirect
from .forms import AutorForm
# Create your views here.


def crearAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')
        #end if
    else:
        autor_form = AutorForm()
    #end if

    return render(request,'prueba/crear_autor.html',{'autor_form':autor_form})
#end def
