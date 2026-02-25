from django.shortcuts import render

# Create your views here.


def HostDashboard(request):
    return render(request,'Host/host_dashboard.html')