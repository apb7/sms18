from django.http import HttpResponse

def index(request):
    return HttpResponse("Trial Home Page")