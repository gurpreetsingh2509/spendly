from django.shortcuts import render
from django.http import HttpResponse

def landing(request):
    return render(request, "landing.html")

def register(request):
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")

def logout(request):
    return HttpResponse("Logout — coming in Step 3")

def profile(request):
    return HttpResponse("Profile page — coming in Step 4")

def add_expense(request):
    return HttpResponse("Add expense — coming in Step 7")

def edit_expense(request, id):
    return HttpResponse(f"Edit expense — coming in Step 8 (ID: {id})")

def delete_expense(request, id):
    return HttpResponse(f"Delete expense — coming in Step 9 (ID: {id})")
