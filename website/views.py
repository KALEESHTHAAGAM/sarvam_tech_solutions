from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")
def services(request):
    return render(request, "service.html")
def service_details(request):
    return render(request, "service-details.html")
def projects(request):
    return render(request, "project.html")

def product_details(request):
    return render(request, "project-details.html")
   
def blog(request):
    return render(request, "news-standard.html")
def contact(request):
    return render(request, "contact.html")