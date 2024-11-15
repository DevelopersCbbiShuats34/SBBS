from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def event(request):
    return render(request, "Events.html")

def about(request):
    return render(request, "AbutUs.html")

def join(request):
    return render(request, "membership.html")

def register(request):
    return render(request, "FAVBS-2024.html")


# test response
def test_(request):
    return HttpResponse(
        """
        <title>Developed By</title>
        <h1>Developed By</h1>
        <a href="https://www.linkedin.com/in/aniket-yadav-085902231/"><h2>@Aniket Yadav (BTech in Bioinformatics)</h2></a>
        <a href="https://www.linkedin.com/in/sharad-kumar-jaiswal-547673132/"><h2>@Sharad Kumar Jaiswal (MTech in Bioinformatics)</a></h2>
        """
        )