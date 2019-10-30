from django.shortcuts import render
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import FormularioLogin
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
"""
Renderiza el template index o página de inicio
"""
def Home(request):
    return render(request,'index.html')#HTTP request
#end def
"""
Valida el login de un usuario
"""
class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)

    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return self.HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request,*args,**kwargs)
        #end if
    #end def

    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)
#end class
"""
Efectua el logout de un usuario
"""
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')
#end def


"""
Valida y renderiza el registro de un usuario
"""
def Registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'registro.html',{'form':form})
#end def
