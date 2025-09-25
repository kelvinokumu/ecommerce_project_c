from django.shortcuts import render

def home(request):
    context = {
        "home_page":"Home page 123",
        "user_name":"Damian"
    }
    
    return render(request, "home.html", context)


def about(request):
    context = {
        "about_page":"About page",
        "is_admin": False
    }
    return render(request, "about.html", context)