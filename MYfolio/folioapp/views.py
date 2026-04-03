from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def resume(request):
    return render(request, 'resume.html')

def service(request):
    return render(request, 'service.html')

def servicespage(request):
    return render(request, 'service.html-page.html')

def portfoliopage(request):
    return render(request, 'portfolio.html-details')



# Create your views here.
