from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .decorator import role_required
# Create your views here.

#@login_required(login_url='login')
@role_required(allowed_roles=["user"])
def UserDashboard(request):
    return render(request,'User/dashboard.html')