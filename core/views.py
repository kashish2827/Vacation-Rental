from django.shortcuts import render,redirect
from .forms import UserSignForm

# Create your views here.
def userSignupView(request):
    if request.method =="POST":
      form = UserSignForm(request.POST or None)
      if form.is_valid():
        form.save()
        return redirect('login') #error
      else:
        return render(request,'core/signup.html',{'form':form})  
    else:
        form = UserSignForm()
        return render(request,'core/signup.html',{'form':form})