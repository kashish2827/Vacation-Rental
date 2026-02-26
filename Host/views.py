from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from User.decorator import role_required
# Create your views here.

#@login_required(login_url='login')
@role_required(allowed_roles=["host"])
def HostDashboard(request):
    return render(request,'Host/host_dashboard.html')