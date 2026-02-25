from django.shortcuts import render

# Create your views here.
def UserDashboard(request):
    return render(request,'User/dashboard.html')